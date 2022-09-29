from fastapi import status,Depends,APIRouter
from sqlalchemy .orm import Session
from Model import schoolProfile
from Authentication import oauth2
from Database.dbconnection import get_db

router = APIRouter()

@router.post("/sclprofile",status_code=status.HTTP_201_CREATED)
def insertdata(Post:dict,db:Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)): 
    print(get_user)
    p=db.query(schoolProfile.Scl_Profile).filter(schoolProfile.Scl_Profile.owner_id==get_user.id)

    if not p.first():
        new = schoolProfile.Scl_Profile(owner_id=get_user.id,**Post)
        db.add(new)
        db.commit()
        db.refresh(new)
        # return {"Data":new.id}
        return{"data":new}
    else:
        p.update(Post,synchronize_session=False)
        db.commit()
        return {"Msg":p.first()} 


@router.get("/sclprofile/")
def retrive_data(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    retrive=db.query(schoolProfile.Scl_Profile).filter(schoolProfile.Scl_Profile.owner_id == get_user.id).first()
    print(retrive)
    return {'sclprofile1':{'instituteName':retrive.instituteName,'postal':retrive.postal,'district':retrive.district,'state':retrive.state,'city':retrive.city,'pincode':retrive.pincode,'url':retrive.url,'officialEmail':retrive.officialEmail,
                            'officialPhone':retrive.officialPhone,'schoolLocation':retrive.schoolLocation,'establishmentYear':retrive.establishmentYear,'medium':retrive.medium},
            'sclprofile2':{'natureOfAffiliation':retrive.natureOfAffiliation,'schoolLevel':retrive.schoolLevel,'gender':retrive.gender,'currentGirls':retrive.currentGirls,'CurrentBoys':retrive.CurrentBoys,'totalStudents':retrive.totalStudents,
                            'teachingStaff':retrive.teachingStaff,'nonTeachingStaff':retrive.nonTeachingStaff,'correspondentName':retrive.correspondentName,'correspondentMobile':retrive.correspondentMobile,'correspondentEmail':retrive.correspondentEmail},
            'sclprofile3':{'principalName':retrive.principalName,'principalPhone':retrive.principalPhone,'principalEmail':retrive.principalEmail,'principalMobile':retrive.principalMobile},
            'sclprofile4':{'instituteRecognizedByGovt':retrive.instituteRecognizedByGovt,'boardName':retrive.boardName,'affiliationNo':retrive.affiliationNo,'affiliationYear':retrive.affiliationYear,'affiliationType':retrive.affiliationType,'affiliationCondition':retrive.affiliationCondition,
                            'minorityStatusCertificate':retrive.minorityStatusCertificate,'christian':retrive.christian,'hindu':retrive.hindu,'muslim':retrive.muslim,
                            'others':retrive.others,'nonBeliever':retrive.nonBeliever,'fireSaftyCertificate':retrive.fireSaftyCertificate,'sanitationCertificate':retrive.sanitationCertificate,'buildingSaftyCertificate':retrive.buildingSaftyCertificate},
            'sclprofile5':{'schoolOwnedBy':retrive.schoolOwnedBy,'trustName':retrive.trustName,'isTrustRegistered':retrive.isTrustRegistered,'act':retrive.act,'registrationYear':retrive.registrationYear,'registrationNo':retrive.registrationNo,'registrationValidity':retrive.registrationValidity,
                            'presidentName':retrive.presidentName,'presidentDesignation':retrive.presidentDesignation,'presidentAddress':retrive.presidentAddress,'presidentPhone':retrive.presidentPhone,'presidentEmail':retrive.presidentEmail},
            'sclprofile6':{'governingBodyOfTrust':retrive.governingBodyOfTrust,'members':retrive.members,'tenureMember':retrive.tenureMember,'epcc':retrive.epcc,'epccMember':retrive.epccMember,'epccTenure':retrive.epccTenure,'parentTeacherAssociation':retrive.parentTeacherAssociation,
                            'parentTeacherAssociationMember':retrive.parentTeacherAssociationMember,'parentTeacherAssociationTenure':retrive.parentTeacherAssociationTenure},
            'sclprofile7':{'studentAssociation':retrive.studentAssociation,'studentAssociationMember':retrive.studentAssociationMember,'studentAssociationTenure':retrive.studentAssociationTenure,'generalComplaintCell':retrive.generalComplaintCell,'schoolManagementCommittee':retrive.schoolManagementCommittee,
                            'constitutionCommittee':retrive.constitutionCommittee,'constitutionMember':retrive.constitutionMember,'constitutionTenure':retrive.constitutionTenure},
            'sclprofile8':{'schoolBuildingType':retrive.schoolBuildingType,'schoolCampusArea':retrive.schoolCampusArea,'builtupArea':retrive.builtupArea,'playGroundArea':retrive.playGroundArea,'noOfBuilding':retrive.noOfBuilding,'provision':retrive.provision,'noOfStaircase':retrive.noOfStaircase,'noOfLifts':retrive.noOfLifts},
            'sclprofile9':{'classRoom':retrive.classRoom,'staffRoom':retrive.staffRoom,'physicsLab':retrive.physicsLab,'chemistryLab':retrive.chemistryLab,'biologyLab':retrive.biologyLab,'mathsLab':retrive.mathsLab,'computerLab':retrive.computerLab,'languageLab':retrive.languageLab,'homeScienceLab':retrive.homeScienceLab,
                            'library':retrive.library,'auditorium':retrive.auditorium,'counselorRoom':retrive.counselorRoom,'visitorParlor':retrive.visitorParlor,'prayerRoom':retrive.prayerRoom,'sickRoom':retrive.sickRoom,'canteen':retrive.canteen,'securityRoom':retrive.securityRoom,'otherRoom':retrive.otherRoom,'staffToilet':retrive.staffToilet,
                            'studentToilet':retrive.studentToilet,'room':retrive.room,'splNeeds':retrive.splNeeds,'staffSpeciallNeed':retrive.staffSpeciallNeed},
            'sclprofile10':{'boundaryWall':retrive.boundaryWall,'wallStatus':retrive.wallStatus,'cctv':retrive.cctv,'dataSaved':retrive.dataSaved,'noOfCamera':retrive.noOfCamera,'maleGuard':retrive.maleGuard,'noOfMaleGuard':retrive.noOfMaleGuard,'femaleGuard':retrive.femaleGuard,'noOfFemaleGuard':retrive.noOfFemaleGuard,
                            'waterFacility':retrive.waterFacility,'drainageFacility':retrive.drainageFacility},
            'sclprofile11':{'midday':retrive.midday,'noOfOwnedBus':retrive.noOfOwnedBus,'gpsCamera':retrive.gpsCamera,'ladyAttendantor':retrive.ladyAttendantor,'firstAid':retrive.firstAid,'drinkingWater':retrive.drinkingWater,'subContractedBus':retrive.subContractedBus,'busPass':retrive.busPass,'freeTransport':retrive.freeTransport},
            'sclprofile12':{'libraryOpen':retrive.libraryOpen,'libraryClose':retrive.libraryClose,'noOfLibraryBook':retrive.noOfLibraryBook,'noOfLibraryMagazine':retrive.noOfLibraryMagazine,'noOfDailies':retrive.noOfDailies,'noOfeBook':retrive.noOfeBook,'onlineAccess':retrive.onlineAccess,'separateLibrary':retrive.separateLibrary,
                            'remedialTeaching':retrive.remedialTeaching,'multimedia1':retrive.multimedia1,'multimedia2':retrive.multimedia2,'multimedia3':retrive.multimedia3,'multimedia4':retrive.multimedia4,'multimedia5':retrive.multimedia5},
            'sclprofile13':{'permanentMalePrincipal':retrive.permanentMalePrincipal,'permanentFemalePrincipal':retrive.permanentFemalePrincipal,'temporaryMalePrincipal':retrive.temporaryMalePrincipal,'temporaryFemalePrincipal':retrive.temporaryFemalePrincipal,'permanentMaleVP':retrive.permanentMaleVP,'permanentFemaleVP':retrive.permanentFemaleVP,
                            'temporaryMaleVP':retrive.temporaryMaleVP,'temporaryFemaleVP':retrive.temporaryFemaleVP,'permanentMalePGT':retrive.permanentMalePGT,'permanentFemalePGT':retrive.permanentFemalePGT,'temporaryMalePGT':retrive.temporaryMalePGT,'temporaryFemalePGT':retrive.temporaryFemalePGT,'permanentMaleTGT':retrive.permanentMaleTGT,
                            'permanentFemaleTGT':retrive.permanentFemaleTGT,'temporaryMaleTGT':retrive.temporaryMaleTGT,'temporaryFemaleTGT':retrive.temporaryFemaleTGT,'permanentMalePRT':retrive.permanentMalePRT,'permanentFemalePRT':retrive.permanentFemalePRT,'temporaryMalePRT':retrive.temporaryMalePRT,'temporaryFemalePRT':retrive.temporaryFemalePRT,
                            'permanentMaleNTT':retrive.permanentMaleNTT,'permanentFemaleNTT':retrive.permanentFemaleNTT,'temporaryMaleNTT':retrive.temporaryMaleNTT,'temporaryFemaleNTT':retrive.temporaryFemaleNTT,'permanentUntrainedMale':retrive.permanentUntrainedMale,'permanentUntrainedFemale':retrive.permanentUntrainedFemale,'temporaryUntrainedMale':retrive.temporaryUntrainedMale,
                            'temporaryUntrainedFemale':retrive.temporaryUntrainedFemale,'permanentMaleLibrarian':retrive.permanentMaleLibrarian,'permanentFemaleLibrarian':retrive.permanentFemaleLibrarian,'temporaryMaleLibrarian':retrive.temporaryMaleLibrarian,'temporaryFemaleLibrarian':retrive.temporaryFemaleLibrarian,'permanentMaleArts':retrive.permanentMaleArts,
                            'permanentFemaleArts':retrive.permanentFemaleArts,'temporaryMaleArts':retrive.temporaryMaleArts,'temporaryFemaleArts':retrive.temporaryFemaleArts,'permanentMaleCounsellor':retrive.permanentMaleCounsellor,'permanentFemaleCounsellor':retrive.permanentFemaleCounsellor,'temporaryMaleCounsellor':retrive.temporaryMaleCounsellor,'temporaryFemaleCounsellor':retrive.temporaryFemaleCounsellor,
                            'permanentMaleLiteracy':retrive.permanentMaleLiteracy,'permanentFemaleLiteracy':retrive.permanentFemaleLiteracy,'temporaryMaleliteracy':retrive.temporaryMaleliteracy,'temporaryFemaleliteracy':retrive.temporaryFemaleliteracy,'permanentMaleMinister':retrive.permanentMaleMinister,'permanentFemaleMinister':retrive.permanentFemaleMinister,'temporaryMaleMinister':retrive.temporaryMaleMinister,
                            'temporaryFemaleMinister':retrive.temporaryFemaleMinister,'permanentMaleNurse':retrive.permanentMaleNurse,'permanentFemaleNurse':retrive.permanentFemaleNurse,'temporaryMaleNurse':retrive.temporaryMaleNurse,'temporaryFemaleNurse':retrive.temporaryFemaleNurse,'permanentMalePT':retrive.permanentMalePT,'permanentFemalePT':retrive.permanentFemalePT,'temporaryMalePT':retrive.temporaryMalePT,'temporaryFemalePT':retrive.temporaryFemalePT},
            'sclprofile14':{'permanentOfficeManager':retrive.permanentOfficeManager,'temporaryOfficeManager':retrive.temporaryOfficeManager,'partTimeOfficeManager':retrive.partTimeOfficeManager,'permanentOfficeAsst':retrive.permanentOfficeAsst,'temporaryOfficeAsst':retrive.temporaryOfficeAsst,'partTimeOfficeAsst':retrive.partTimeOfficeAsst,'permanentClerk':retrive.permanentClerk,'temporaryClerk':retrive.temporaryClerk,'partTimeClerk':retrive.partTimeClerk,
                            'permanentLabAttendant':retrive.permanentLabAttendant,'temporaryLabAttendant':retrive.temporaryLabAttendant,'partTimeLabAttendant':retrive.partTimeLabAttendant,'permanentAccountant':retrive.permanentAccountant,'temporaryAccountant':retrive.temporaryAccountant,'partTimeAccountant':retrive.partTimeAccountant,'permanentPeon':retrive.permanentPeon,'temporaryPeon':retrive.temporaryPeon,'partTimePeon':retrive.partTimePeon,
                            'permanentOthers':retrive.permanentOthers,'temporaryOthers':retrive.temporaryOthers,'partTimeOthers':retrive.partTimeOthers},
            'sclprofile15':{'noOfCarricularActivity':retrive.noOfCarricularActivity,'noOfGrps':retrive.noOfGrps,'noOfCommunity':retrive.noOfCommunity,'noOfSportsAtSchool':retrive.noOfSportsAtSchool,'noOfSportsAtZonal':retrive.noOfSportsAtZonal,'noOfSportsAtDist':retrive.noOfSportsAtDist,'noOfSportsAtState':retrive.noOfSportsAtState,'noOfSportsAtNational':retrive.noOfSportsAtNational,'noOfSportsAtInternational':retrive.noOfSportsAtInternational,
                            'noOfCompetitionAtSchool':retrive.noOfCompetitionAtSchool,'noOfCompetitionAtZonal':retrive.noOfCompetitionAtZonal,'noOfCompetitionAtDist':retrive.noOfCompetitionAtDist,'noOfCompetitionAtState':retrive.noOfCompetitionAtState,'noOfCompetitionAtNational':retrive.noOfCompetitionAtNational,'noOfCompetitionAtInternational':retrive.noOfCompetitionAtInternational,'noOfSclProgramsAtSchool':retrive.noOfSclProgramsAtSchool,
                            'noOfSclProgramsAtZonal':retrive.noOfSclProgramsAtZonal,'noOfSclProgramsAtDist':retrive.noOfSclProgramsAtDist,'noOfSclProgramsAtState':retrive.noOfSclProgramsAtState,'noOfSclProgramsAtNational':retrive.noOfSclProgramsAtNational,'noOfSclProgramsAtInternational':retrive.noOfSclProgramsAtInternational},
            'sclprofile16':{'academicYearBeginingMonth':retrive.academicYearBeginingMonth,'academicYearEndingMonth':retrive.academicYearEndingMonth,'workingDay2021':retrive.workingDay2021,'workingDay2020':retrive.workingDay2020,'workingDay2019':retrive.workingDay2019,'hrsOfAcademic2021':retrive.hrsOfAcademic2021,'hrsOfAcademic2020':retrive.hrsOfAcademic2020,'hrsOfAcademic2019':retrive.hrsOfAcademic2019,'instructionalHrs2021':retrive.instructionalHrs2021,
                            'instructionalHrs2020':retrive.instructionalHrs2020,'instructionalHrs2019':retrive.instructionalHrs2019,'nonInstructuionalWorkingday2021':retrive.nonInstructuionalWorkingday2021,'nonInstructuionalWorkingday2020':retrive.nonInstructuionalWorkingday2020,'nonInstructuionalWorkingday2019':retrive.nonInstructuionalWorkingday2019,'holiday2021':retrive.holiday2021,'holiday2020':retrive.holiday2020,'holiday2019':retrive.holiday2019},
            'sclprofile17':{'noOfSubTeachingPeriod':retrive.noOfSubTeachingPeriod,'noOfMoralTeachingPeriod':retrive.noOfMoralTeachingPeriod,'teachingDuration':retrive.teachingDuration,'noOfClubHrs':retrive.noOfClubHrs,'fromTimeInSummer':retrive.fromTimeInSummer,'toTimeInSummer':retrive.toTimeInSummer,'fromTimeInWinter':retrive.fromTimeInWinter,'toTimeInWinter':retrive.toTimeInWinter,'shift':retrive.shift},
            }

