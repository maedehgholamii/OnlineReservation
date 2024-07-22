





class BeautyJob(Base):
    __tablename__ = "beauty_job_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(20), nullable=False, unique=True)
    _image = Column("image", String(50))
    _description = Column("description", String(100))

    def __init__(self, title, image,description):
        self._id = None
        self._title = title
        self._image = image
        self._description = description

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = name_validator(title, "Invalid Title!!")

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description_validator(description, "Invalid Description!!")
