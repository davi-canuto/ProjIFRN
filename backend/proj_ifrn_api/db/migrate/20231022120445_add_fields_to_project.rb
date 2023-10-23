class AddFieldsToProject < ActiveRecord::Migration[7.0]
  def change
    add_column :projects, :external_url, :string
    add_column :projects, :short_description, :string
    add_column :projects, :name, :string
    add_column :projects, :keywords, :string, array: true
    add_column :projects, :start_at, :datetime
    add_column :projects, :end_at, :datetime
    add_column :projects, :phase, :integer
  end
end
