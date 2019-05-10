class BinarySearchTree:
  def __init__(self, name, value):
    self.name = name
    self.value = value
    self.left = None
    self.right = None

  def insert(self, name, value):
    if value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(name, value)
      else:
        self.left.insert(name, value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(name, value)
      else:
        self.right.insert(name, value)

  def contains(self, name, value):
    if value == self.value and name == self.name:
      return True
    elif self.left is None and self.right is None:
      return False
    elif self.left and value < self.value:
      return self.left.contains(name, value)
    elif self.right and value > self.value:
      return self.right.contains(name, value)


  def get_max(self):
    if not self.right:
      return self.value
    else:
      return self.right.get_max()

  def for_each(self, cb):
    cb(self.value)
    if self.right:
      self.right.for_each(cb)
    if self.left:
      self.left.for_each(cb)
