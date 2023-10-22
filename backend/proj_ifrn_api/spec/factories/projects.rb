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
FactoryBot.define do
  factory :project do
    title { 'ProjIFRN Title' }
    name { 'ProjIFRN' }
    description { 'ProjIFRN description project' }
    content { 'content' }
    status { :in_progress }
    external_url { "htts://" }
    short_description { 'ProjIFRN short description' }
    keywords { 'corporative' }
    start_at { Time.zone.now - 1.month }
    end_at { Time.zone.now + 1.month }
    phase { :distributed }
  end
end
