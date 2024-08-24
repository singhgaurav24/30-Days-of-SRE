provider "github" {
    token = "your github token"
  
}

resource "github_repository" "terrform-first-repo" {
  name        = "first-repo-using-terraform"
  description = "My first repo using terrform"
  visibility = "public"
  auto_init = true
}