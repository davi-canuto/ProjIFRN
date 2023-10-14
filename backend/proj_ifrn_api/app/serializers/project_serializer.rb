class ProjectSerializer < ActiveModel::Serializer
  attributes :id, :created_at, :updated_at, :title, :description, :content, :status
end
