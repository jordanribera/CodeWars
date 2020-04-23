def is_isogram(string)
  return string.downcase.chars.uniq.count == string.chars.count
end
