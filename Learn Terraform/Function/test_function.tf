variable users {
  type = list
}

output printJoin {
  value = "${join("-->" , var.users)}"
}

output printUpper {
  value = "${upper(var.users[1])}"
}

output printlower {
  value = "${lower(var.users[2])}"
}

output printTitle {
  value = "${title(var.users[0])}"
}
