class CreatePosts < ActiveRecord::Migration
  def change
    create_table :posts do |t|
      t.string :title
      t.text :content
      t.references :blog, index: true

      t.timestamps null: false
    end
    add_foreign_key :posts, :blogs
  end
end
