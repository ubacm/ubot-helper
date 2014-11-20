class Vcf(object):
  def __init__(self, raw_vcf_str):
    self.vcf_lines = raw_vcf_str.split('\n')[:-2]
    self.process()

  def process(self):
    for line in self.vcf_lines:
      key, value = line.split(':')
      if key == 'FN':
        self.name = value
      if key == 'ORG':
        self.uni, self.major = value.split(';')
      if key == 'TITLE':
        self.title = value

  def __str__(self):
    return '''
    Name: %s
    Major: %s
    Title: %s
    ''' % (self.name, self.major, self.title)
