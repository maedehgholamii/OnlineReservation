from controller.exceptions.exceptions  import BeautyJobNotFoundError
from model.da.da import *
from model.entity.beauty_job import BeautyJob

class BeautyJobService:
    @staticmethod
    def save(beauty_job):
        beauty_job_da = DataAccess(BeautyJob)
        beauty_job_da.save(beauty_job)
        return beauty_job

    @staticmethod
    def edit(beauty_job):
        beauty_job_da = DataAccess(beauty_job)
        if beauty_job_da.find_by_id(beauty_job.id):
            beauty_job_da.edit(beauty_job)
            return beauty_job
        else:
            raise BeautyJobNotFoundError()

    @staticmethod
    def remove(id):
        beauty_job_da = DataAccess(BeautyJob)
        if beauty_job_da.find_by_id(id):
            return beauty_job_da.remove(id)
        else:
            raise BeautyJobNotFoundError()

    @staticmethod
    def find_all():
        beauty_job_da = DataAccess(BeautyJob)
        return beauty_job_da.find_all()

    @staticmethod
    def find_by_id(id):
        beauty_job_da = DataAccess(BeautyJob)
        return beauty_job_da.find_by_id(id)


    @staticmethod
    def find_by_title(title):
        beauty_job_da = DataAccess(BeautyJob)
        return beauty_job_da.find_by(BeautyJob.title == title)

    @staticmethod
    def find_by_image(image):
        beauty_job_da = DataAccess(BeautyJob)
        return beauty_job_da.find_by(BeautyJob.image == image)

    @staticmethod
    def find_by_description(description):
        beauty_job_da = DataAccess(BeautyJob)
        return beauty_job_da.find_by(BeautyJob.description == description)

