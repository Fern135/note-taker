#!/usr/bin/env python3


import os
import platform
import asyncio
import sys

async def create_env_file(env_path, content):
    """Generate a .env file with specific content in a specific directory."""
    with open(env_path, 'w') as file:
        file.write(content)
    print(f"Created .env file at {env_path}")

async def create_virtual_environment():
    """Create a virtual environment depending on the operating system."""
    venv_command = f"{sys.executable} -m venv venv"
    print("Creating virtual environment...")
    await asyncio.create_subprocess_shell(venv_command)

    activate_script = (
        'venv\\Scripts\\activate.bat' if platform.system() == 'Windows' else 'source venv/bin/activate'
    )

    return activate_script

async def activate_virtual_environment(activate_command):
    """Activate the virtual environment and install dependencies."""
    print("Activating virtual environment...")

    # Prepare the pip install command
    pip_install_command = f"{activate_command} && pip install -r requirements.txt"

    # Run the activation script and install requirements
    if platform.system() == 'Windows':
        await asyncio.create_subprocess_shell(pip_install_command, shell=True)
    else:
        await asyncio.create_subprocess_shell(pip_install_command, shell=True, executable='/bin/bash')

async def run_django_commands():
    """Run Django setup commands: makemigrations, migrate, and runserver."""
    commands = [
        'python manage.py collectstatic',
        'python manage.py makemigrations',
        'python manage.py migrate',
        'python manage.py runserver'
    ]

    tasks = [asyncio.create_subprocess_shell(command, shell=True) for command in commands]

    # Run commands concurrently
    await asyncio.gather(*tasks)

async def main():
    # Set the path and content for the .env file
    env_directory = os.path.join(os.getcwd())  # Set to current working directory
    env_path = os.path.join(env_directory, '.env')
    env_content = """
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/mydatabase
    """

    # Run .env file creation and virtual environment creation concurrently
    create_env_task = create_env_file(env_path, env_content)
    create_venv_task = create_virtual_environment()

    # Execute both tasks concurrently
    activate_script, _ = await asyncio.gather(create_venv_task, create_env_task)

    # Activate the virtual environment and install dependencies
    await activate_virtual_environment(activate_script)

    # Run Django commands concurrently
    await run_django_commands()


if __name__ == "__main__":
    asyncio.run(main())
