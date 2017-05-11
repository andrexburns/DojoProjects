#number to string
arr = [-1, -3, 2]
puts arr.each_index { |index| arr[index]="Dojo" if arr[index] < 0 }
