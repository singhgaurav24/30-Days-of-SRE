variable "userAge" {
  type = map
  default = {
    Gaurav = 26
    Amrit  = 25
    Praksh = 24
    Akshit = 23
  }
}

variable "userName" {
  type = string
}

output print {
  value = "Age of ${var.userName} ${lookup(var.userAge, "${var.userName}")}"
}