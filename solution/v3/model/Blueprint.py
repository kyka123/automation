
class Blueprint:

  def __init__(self, inst):
     self.instance = inst

  @property
  def name(self):
     return self.instance['status']['name']

  @property
  def description(self):
     return self.instance['status']['description']

  @property
  def uuid(self):
     return self.instance['status']['uuid']

  @property
  def state(self):
     return self.instance['status']['state']

  @property
  def project(self):
     return self.instance['metadata']['project_reference']['name']

  @property
  def project_uuid(self):
     return self.instance['status']['uuid']

  @property
  def owner(self):
     return self.instance['metadata']['owner_reference']['name']


  def show(self):
     print 'name: ' +  self.name
     #print 'description: ' + self.description
     print 'uuid: ' +  self.uuid
     print 'state: ' + self.state
     print 'project: ' +  self.project
     print 'project_uuid: ' + self.project_uuid
     print 'owner: ' + self.owner
     print ' '