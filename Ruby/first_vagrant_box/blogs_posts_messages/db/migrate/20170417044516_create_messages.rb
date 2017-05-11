class CreateMessages < ActiveRecord::Migration
  def change
    create_table :messages do |t|
      t.integer :post_id
      t.string :author
      t.string :message

      t.timestamps null: false
    end
  end
end
