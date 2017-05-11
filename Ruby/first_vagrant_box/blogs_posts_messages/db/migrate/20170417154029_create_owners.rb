class CreateOwners < ActiveRecord::Migration
  def change
    create_table :owners do |t|
      t.integer :user_id
      t.integer :blog_id

      t.timestamps null: false
    end
  end
end
