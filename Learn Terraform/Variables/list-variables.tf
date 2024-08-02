variable users {
  type = list
}

output printfirstUser {
  value = "The first user is ${var.users[0]}"
}

output printSecondUser {
  value = "The second user is ${var.users[1]}"
}