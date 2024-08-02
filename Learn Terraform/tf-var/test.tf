variable age {
  type = map
}

variable "userName" {
  type = string
}

output "print" {
  value = "Age of ${var.userName} is ${lookup(var.age,"${var.userName}")}"
}
