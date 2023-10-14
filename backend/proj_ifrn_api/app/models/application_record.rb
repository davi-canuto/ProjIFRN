class ApplicationRecord < ActiveRecord::Base
  primary_abstract_class

  def serialized(serializer = nil, scope = {})
    serializer ||= self.class.default_serializer
    serializer.new(self, scope: scope)
  end

  def self.serialized(serializer = nil, scope = {})
    serializer ||= default_serializer
    where('').to_a.serialized(serializer, scope)
  end

  def self.default_serializer
    "#{self}Serializer".constantize
  end
end
