from model.entity.beauty_job import BeautyJob
from model.service.beauty_job_service import BeautyJobService
from model.tools.decorators import exception_handling
from model.tools.logger import Logger

class BeautyJobController:
    @classmethod
    @exception_handling
    def save(cls,title,image,description):
        beauty_job = BeautyJob(title,image,description)
        BeautyJobService.save(beauty_job)
        return True, beauty_job

    @classmethod
    @exception_handling
    def edit(cls,id,title,image,description):
        beauty_job = BeautyJob(id,title,image,description)
        beauty_job.id = id
        BeautyJobService.edit(beauty_job)
        return True, beauty_job

    @classmethod
    def remove(cls,id):
        beauty_job = BeautyJobService.remove(id)
        Logger.info(f"BeautyJob Removed - {beauty_job}")
        return True, beauty_job

    @classmethod
    @exception_handling
    def find_all(cls,):
        beauty_job_list = BeautyJobService.find_all()
        Logger.info(f"BeautyJob FindAll()")
        return True, beauty_job_list

    @classmethod
    @exception_handling
    def find_by_id(cls,id):
        beauty_job = BeautyJobService.find_by_id(id)
        Logger.info(f"BeautyJob Find By Id({id})")
        return True, beauty_job