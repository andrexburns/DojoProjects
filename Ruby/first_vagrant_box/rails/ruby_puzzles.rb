#Create an array with the following values: 3,5,1,2,7,9,8,13,25,32. Print the sum of all numbers in the array. Also have the function return an array that only include numbers that are greater than 10 (e.g. when you pass the array above, it should return an array with the values of 13,25,32 - hint: use reject or find_all method)
numbers_array = [3,5,1,2,7,9,8,13,25,32]
puts numbers_array
puts numbers_array.reduce(:+)
puts numbers_array.reject{|number| number > 10}

persons_array = ["Jim","Kerub","Oliver", "Kelly", "Matt","Brian"]
puts persons_array
persons_array.shuffle.each { |person| puts person }
puts persons_array.select { |person| person.length }

letters_array = ("A".."Z").to_a
puts letters_array
puts letters_array.shuffle.last
puts letters_array.shuffle.first

shuffled = letters_array.shuffle
puts "#{shuffled.first} is a vowel" if ["A","E","I","O","U"].include? shuffled.first
# OR puts rand(10)
puts (rand() * 10).to_i

random_array = []
10.times{random_array << rand(55..100)}
puts random_array
puts random_array.sort
puts random_array.min
puts random_array.max

string_array = []
10.times do
  str = ""
  5.times{string_array << (65+rand(26)).chr}
  string_array << str
end
puts string_array
