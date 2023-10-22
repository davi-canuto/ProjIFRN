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
class Project < ApplicationRecord
  enum status: { in_progress: 0, closed: 1, finished: 2 }
  enum phase: { web: 0, distributed: 1, corporative: 2 }
end
