class Project
  attr_reader :name, :description

  def initialize(name, description)
    @name = name
    @description = description
  end

  def elevator_pitch
    "#{@name}, #{@description}"
  end
end

project1 = Project.new("project1","description1")
puts project1.name
puts project1.elevator_pitch
