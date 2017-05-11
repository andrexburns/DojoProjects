class CreateBlogs < ActiveRecord::Migration
  def change
    create_table :blogs do |t|
      t.string :first_name
      t.string :last_name
      t.string :description

      t.timestamps null: false
    end
  end
end
