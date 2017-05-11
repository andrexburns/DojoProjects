class CreateMessages < ActiveRecord::Migration
  def change
    create_table :messages do |t|
      t.string :author
      t.text :message
      t.references :post, index: true

      t.timestamps null: false
    end
    add_foreign_key :messages, :posts
  end
end
