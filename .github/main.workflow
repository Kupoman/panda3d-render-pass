workflow "CI/CD" {
  on = "push"
  resolves = ["Test"]
}

action "Test" {
  uses = "./.github/actions/poetry"
  runs = "make ci"
}

