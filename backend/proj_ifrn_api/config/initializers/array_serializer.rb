Array.class_eval do
  def serialized serializer = nil, scope = {}
    return [] if self.empty?
    klass = self.first.class.to_s
    serializer ||= "#{klass}Serializer".constantize
    self.map do |object|
      object.serialized(serializer, scope)
    end
  end
end