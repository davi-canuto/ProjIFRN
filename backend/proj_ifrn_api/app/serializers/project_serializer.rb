# == Schema Information
#
# Table name: projects
#
#  id                :integer          not null, primary key
#  title             :string
#  description       :string
#  content           :string
#  status            :integer
#  created_at        :datetime         not null
#  updated_at        :datetime         not null
#  external_url      :string
#  short_description :string
#  name              :string
#  keywords          :string
#  start_at          :datetime
#  end_at            :datetime
#  phase             :integer
#
class ProjectSerializer < ActiveModel::Serializer
  attributes :id, :created_at, :updated_at, :title, :description, :content, :status, :name,
             :external_url, :short_description, :keywords, :start_at, :end_at, :phase
end
