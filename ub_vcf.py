class Vcf(object):
  def __init__(self, raw_vcf_str):
    self.vcf_lines = raw_vcf_str.split('\n')[:-2]
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
      if key == 'URL':
        self.website = value
      if 'EMAIL' in key:
        self.email = value

  def __str__(self):
    return '''
    Name: %s
    Major: %s
    Title: %s
    Website: %s
    Email: %s
    ''' % (self.name, self.major, self.title, self.website, self.email)
