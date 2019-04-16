workflow "Test on push" {
  resolves = ["Test"]
  on = "push"
}

action "Test" {
  uses = "./.github/actions/poetry"
  runs = "make ci"
}

workflow "Publish on release" {
  on = "release"
  resolves = ["pypi"]
}

action "pypi" {
  uses = "./.github/actions/poetry"
  secrets = ["PYPI_USERNAME", "PYPI_PASSWORD"]
  args = "make publish"
}
