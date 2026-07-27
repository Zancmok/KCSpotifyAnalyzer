import tempfile
import venv
from pathlib import Path
from dataclasses import dataclass
import subprocess
import sys
from typing import Optional


@dataclass(frozen=True)
class Project:
    """
    Represents a Python project to be analyzed with pylint.

    Attributes:
        name: Name of the project.
        project_path: Path to the project's source directory.
        config_path: Path to the project's pylint configuration file.
        dependencies_path: Path to the project's requirements file, if any.
        project_dependencies: Other projects that must be installed before
            analyzing this project.
        installable: Whether the project itself should be installed into the
            temporary virtual environment.
    """
    name: str
    project_path: Path
    config_path: Path
    dependencies_path: Optional[Path]
    project_dependencies: list[Project]
    installable: bool


PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent
SRC_FOLDER: Path = Path(PROJECT_ROOT, "src")
DOCKER_FOLDER: Path = Path(PROJECT_ROOT, "docker")
PYLINT_SUFFIX: str = ".pylintrc"
REQUIREMENTS_SUFFIX: str = "requirements.txt"


def define_project(project_name: str, project_dependencies: list[Project], include_dependencies: bool = True,
                   installable: bool = False) -> Project:
    """
    Create a project configuration used for pylint execution.

    Args:
        project_name: Name of the project located inside the source directory.
        project_dependencies: Other projects that need to be installed before
            linting this project.
        include_dependencies: Whether to include a requirements.txt file from
            the docker configuration directory.
        installable: Whether the project itself should be installed.

    Returns:
        A configured Project instance.
    """
    return Project(
        project_name,
        Path(SRC_FOLDER, project_name),
        Path(SRC_FOLDER, project_name, PYLINT_SUFFIX),
        Path(DOCKER_FOLDER, project_name, REQUIREMENTS_SUFFIX) if include_dependencies else None,
        project_dependencies,
        installable
    )


database_lib: Project = define_project(
    "database_lib",
    [],
    include_dependencies=False,
    installable=True,
)
PROJECTS: list[Project] = [
    database_lib,
    define_project("data_analyzer", [database_lib]),
    define_project("web_server", [database_lib])
]


def install_pylint(python: Path) -> None:
    """
    Install pylint into the specified Python environment.

    Args:
        python: Path to the Python executable of the virtual environment.

    Raises:
        subprocess.CalledProcessError: If pylint installation fails.
    """
    subprocess.run(
        [
            python,
            "-m",
            "pip",
            "install",
            "pylint",
        ],
        check=True,
    )


def install_requirements(python: Path, requirements: Path) -> None:
    """
    Install project dependencies from a requirements file.

    Args:
        python: Path to the Python executable of the virtual environment.
        requirements: Path to the requirements.txt file.

    Raises:
        subprocess.CalledProcessError: If dependency installation fails.
    """
    subprocess.run(
        [
            python,
            "-m",
            "pip",
            "install",
            "-r",
            str(requirements),
        ],
        check=True,
    )


def install_project(python: Path, project_path: Path) -> None:
    """
    Install a local Python project in editable mode.

    Args:
        python: Path to the Python executable of the virtual environment.
        project_path: Path to the project to install.

    Raises:
        subprocess.CalledProcessError: If project installation fails.
    """
    subprocess.run(
        [
            python,
            "-m",
            "pip",
            "install",
            "-e",
            str(project_path),
        ],
        check=True,
    )


def get_venv_python(venv_path: Path) -> Path:
    """
    Get the path to the Python executable inside a virtual environment.

    Args:
        venv_path: Path to the virtual environment directory.

    Returns:
        Path to the virtual environment's Python executable.
    """
    if sys.platform == "win32":
        return venv_path / "Scripts" / "python.exe"

    return venv_path / "bin" / "python"


def run_pylint(project: Project) -> int:
    """
    Run pylint for a project inside an isolated virtual environment.

    Creates a temporary virtual environment, installs pylint, installs all
    required dependencies, and executes pylint using the project's configuration.

    Args:
        project: Project configuration to analyze.

    Returns:
        The pylint process return code. A value of zero indicates success.
    """
    with tempfile.TemporaryDirectory() as tmp:
        print(f"Running pylint for {project.name}...")

        print("Creating venv")
        venv_path: Path = Path(tmp) / "venv"

        venv.create(
            venv_path,
            with_pip=True
        )

        venv_python: Path = get_venv_python(venv_path)

        print("Installing pylint")
        install_pylint(venv_python)

        if project.dependencies_path:
            print("Installing requirements")
            install_requirements(
                venv_python,
                project.dependencies_path
            )

        print("Installing project dependencies")
        for project_dependency in project.project_dependencies:
            install_project(
                venv_python,
                project_dependency.project_path
            )

        if project.installable:
            print("Installing project")
            install_project(
                venv_python,
                project.project_path
            )

        print("Running pylint")
        cmd: list[str | Path] = [
            venv_python,
            "-m",
            "pylint",
            "--rcfile",
            project.config_path,
            project.project_path if not project.installable else project.project_path / project.name,
        ]

        result: subprocess.CompletedProcess[bytes] = subprocess.run(cmd, check=False)

        return result.returncode


def main() -> None:
    """
    Run pylint checks for all configured projects.

    Executes pylint independently for each project and exits with a non-zero
    status code if any project fails linting.
    """
    failed: list[Project] = []

    for project in PROJECTS:
        code = run_pylint(project)

        if code != 0:
            failed.append(project)

    if failed:
        print("\nFailed projects:")
        for project in failed:
            print(f"- {project.name}")

        sys.exit(1)

    print("\nAll pylint checks passed.")


if __name__ == "__main__":
    main()
