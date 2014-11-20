class Vcf(object):
  def __init__(self, raw_vcf_str):
    self.vcf_lines = raw_vcf_str.split('\n')[:-1]
    self.name = 'N/A'
    self.uni = 'N/A'
    self.major = 'N/A'
    self.title = 'N/A'
    self.website = 'N/A'
    self.email = 'N/A'
    self.unknown = len(self.vcf_lines) == 5
    if not self.unknown:
      self.process()

  def process(self):
    for line in self.vcf_lines:
      key, value = line.split(':', 1)
      if key == 'FN':
        self.name = value
      if key == 'ORG':
        self.uni, self.major = value.split(';')
      if key == 'TITLE':
        self.title = value
      if 'URL' in key:
        self.website = value
      if 'EMAIL' in key:
        self.email = value

  def __str__(self):
    if self.unknown:
      return 'User does not exist.'
    return '''
    Name: %s
    Major: %s
    Title: %s
    Website: %s
    Email: %s
    ''' % (self.name, self.major, self.title, self.website, self.email)
