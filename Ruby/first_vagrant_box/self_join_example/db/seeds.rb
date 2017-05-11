users = [["joe","smith","joe@gmail.com","foobars"],["kim","smith","kim@gmail.com","foobars"],["jimmy","jones","jimmy@gmail.com","foobars"],["dave","stanton","dave@gmail.com","foobars"]]

users.each do |first_name, last_name, email, password|
  User.create(first_name: first_name, last_name: last_name, email: email, password: password)
end
