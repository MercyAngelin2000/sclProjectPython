from fastapi import status,Depends,APIRouter
from sqlalchemy .orm import Session
from Model import schoolProfile
from Authentication import oauth2
from Database.dbconnection import get_db

router = APIRouter()
global i

def getData(data):
    temp=[]
    scholarship=[]    

    for value in data:
        keys =value.keys()
        break

    for value in data:
        for key in keys:
            temp.append(value[key])
        scholarship.append(temp)
        temp=[]

    return scholarship

# def retrow(data):
#     scholarship=[]
#     key = ("scholarshipName","boy","girl","byGovt","byPrivate")
    
#     for i in data:
#         print(i)
#         my_dict = dict(zip(key,i))
#         scholarship.append(my_dict)
#     print(scholarship)
#     return scholarship
   

    

@router.post("/sclprofile",status_code=status.HTTP_201_CREATED)
def insertdata(Post:dict,db:Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)): 
    print(get_user)
    p=db.query(schoolProfile.Scl_Profile).filter(schoolProfile.Scl_Profile.owner_id==get_user.id)

    if not p.first():
        print(Post)
        new = schoolProfile.Scl_Profile(owner_id=get_user,**Post)
        db.add(new)
        db.commit()
        db.refresh(new)
        return{"data":new}
    else:     
        if (Post.get('scholarship')):
            Post['scholarship'] = getData(Post['scholarship'])   
            print(Post)
        p.update(Post,synchronize_session=False)
        db.commit()
        return {"Msg":p.first()} 


@router.get("/sclprofile/")
def retrieve_data(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    retrieve=db.query(schoolProfile.Scl_Profile).filter(schoolProfile.Scl_Profile.owner_id == get_user.id).first()
    print(retrieve)
    if retrieve:
        print(retrieve.scholarship)
        return {'sclprofile1':{'instituteName':retrieve.instituteName,'postal':retrieve.postal,'district':retrieve.district,'state':retrieve.state,'city':retrieve.city,'pincode':retrieve.pincode,'url':retrieve.url,'officialEmail':retrieve.officialEmail,
                            'officialPhone':retrieve.officialPhone,'schoolLocation':retrieve.schoolLocation,'establishmentYear':retrieve.establishmentYear,'medium':retrieve.medium},
            'sclprofile2':{'natureOfAffiliation':retrieve.natureOfAffiliation,'schoolLevel':retrieve.schoolLevel,'gender':retrieve.gender,'currentGirls':retrieve.currentGirls,'CurrentBoys':retrieve.CurrentBoys,'totalStudents':retrieve.totalStudents,
                            'teachingStaff':retrieve.teachingStaff,'nonTeachingStaff':retrieve.nonTeachingStaff,'correspondentName':retrieve.correspondentName,'correspondentMobile':retrieve.correspondentMobile,'correspondentEmail':retrieve.correspondentEmail},
            'sclprofile3':{'principalName':retrieve.principalName,'principalPhone':retrieve.principalPhone,'principalEmail':retrieve.principalEmail,'principalMobile':retrieve.principalMobile},
            'sclprofile4':{'instituteRecognizedByGovt':retrieve.instituteRecognizedByGovt,'boardName':retrieve.boardName,'affiliationNo':retrieve.affiliationNo,'affiliationYear':retrieve.affiliationYear,'affiliationType':retrieve.affiliationType,'affiliationCondition':retrieve.affiliationCondition,
                            'minorityStatusCertificate':retrieve.minorityStatusCertificate,'christian':retrieve.christian,'hindu':retrieve.hindu,'muslim':retrieve.muslim,
                            'others':retrieve.others,'nonBeliever':retrieve.nonBeliever,'fireSaftyCertificate':retrieve.fireSaftyCertificate,'sanitationCertificate':retrieve.sanitationCertificate,'buildingSaftyCertificate':retrieve.buildingSaftyCertificate},
            'sclprofile5':{'schoolOwnedBy':retrieve.schoolOwnedBy,'trustName':retrieve.trustName,'isTrustRegistered':retrieve.isTrustRegistered,'act':retrieve.act,'registrationYear':retrieve.registrationYear,'registrationNo':retrieve.registrationNo,'registrationValidity':retrieve.registrationValidity,
                            'presidentName':retrieve.presidentName,'presidentDesignation':retrieve.presidentDesignation,'presidentAddress':retrieve.presidentAddress,'presidentPhone':retrieve.presidentPhone,'presidentEmail':retrieve.presidentEmail},
            'sclprofile6':{'governingBodyOfTrust':retrieve.governingBodyOfTrust,'members':retrieve.members,'tenureMember':retrieve.tenureMember,'epcc':retrieve.epcc,'epccMember':retrieve.epccMember,'epccTenure':retrieve.epccTenure,'parentTeacherAssociation':retrieve.parentTeacherAssociation,
                            'parentTeacherAssociationMember':retrieve.parentTeacherAssociationMember,'parentTeacherAssociationTenure':retrieve.parentTeacherAssociationTenure},
            'sclprofile7':{'studentAssociation':retrieve.studentAssociation,'studentAssociationMember':retrieve.studentAssociationMember,'studentAssociationTenure':retrieve.studentAssociationTenure,'generalComplaintCell':retrieve.generalComplaintCell,'schoolManagementCommittee':retrieve.schoolManagementCommittee,
                            'constitutionCommittee':retrieve.constitutionCommittee,'constitutionMember':retrieve.constitutionMember,'constitutionTenure':retrieve.constitutionTenure},
            'sclprofile8':{'schoolBuildingType':retrieve.schoolBuildingType,'schoolCampusArea':retrieve.schoolCampusArea,'builtupArea':retrieve.builtupArea,'playGroundArea':retrieve.playGroundArea,'noOfBuilding':retrieve.noOfBuilding,'provision':retrieve.provision,'noOfStaircase':retrieve.noOfStaircase,'noOfLifts':retrieve.noOfLifts},
            'sclprofile9':{'classRoom':retrieve.classRoom,'staffRoom':retrieve.staffRoom,'physicsLab':retrieve.physicsLab,'chemistryLab':retrieve.chemistryLab,'biologyLab':retrieve.biologyLab,'mathsLab':retrieve.mathsLab,'computerLab':retrieve.computerLab,'languageLab':retrieve.languageLab,'homeScienceLab':retrieve.homeScienceLab,
                            'library':retrieve.library,'auditorium':retrieve.auditorium,'counselorRoom':retrieve.counselorRoom,'visitorParlor':retrieve.visitorParlor,'prayerRoom':retrieve.prayerRoom,'sickRoom':retrieve.sickRoom,'canteen':retrieve.canteen,'securityRoom':retrieve.securityRoom,'otherRoom':retrieve.otherRoom,'staffToilet':retrieve.staffToilet,
                            'studentToilet':retrieve.studentToilet,'room':retrieve.room,'splNeeds':retrieve.splNeeds,'staffSpeciallNeed':retrieve.staffSpeciallNeed},
            'sclprofile10':{'boundaryWall':retrieve.boundaryWall,'wallStatus':retrieve.wallStatus,'cctv':retrieve.cctv,'dataSaved':retrieve.dataSaved,'noOfCamera':retrieve.noOfCamera,'maleGuard':retrieve.maleGuard,'noOfMaleGuard':retrieve.noOfMaleGuard,'femaleGuard':retrieve.femaleGuard,'noOfFemaleGuard':retrieve.noOfFemaleGuard,
                            'waterFacility':retrieve.waterFacility,'drainageFacility':retrieve.drainageFacility},
            'sclprofile11':{'midday':retrieve.midday,'noOfOwnedBus':retrieve.noOfOwnedBus,'gpsCamera':retrieve.gpsCamera,'ladyAttendantor':retrieve.ladyAttendantor,'firstAid':retrieve.firstAid,'drinkingWater':retrieve.drinkingWater,'subContractedBus':retrieve.subContractedBus,'busPass':retrieve.busPass,'freeTransport':retrieve.freeTransport},
            'sclprofile12':{'libraryOpen':retrieve.libraryOpen,'libraryClose':retrieve.libraryClose,'noOfLibraryBook':retrieve.noOfLibraryBook,'noOfLibraryMagazine':retrieve.noOfLibraryMagazine,'noOfDailies':retrieve.noOfDailies,'noOfeBook':retrieve.noOfeBook,'onlineAccess':retrieve.onlineAccess,'separateLibrary':retrieve.separateLibrary,
                            'remedialTeaching':retrieve.remedialTeaching,'multimedia1':retrieve.multimedia1,'multimedia2':retrieve.multimedia2,'multimedia3':retrieve.multimedia3,'multimedia4':retrieve.multimedia4,'multimedia5':retrieve.multimedia5},
            'sclprofile13':{'permanentMalePrincipal':retrieve.permanentMalePrincipal,'permanentFemalePrincipal':retrieve.permanentFemalePrincipal,'temporaryMalePrincipal':retrieve.temporaryMalePrincipal,'temporaryFemalePrincipal':retrieve.temporaryFemalePrincipal,'permanentMaleVP':retrieve.permanentMaleVP,'permanentFemaleVP':retrieve.permanentFemaleVP,
                            'temporaryMaleVP':retrieve.temporaryMaleVP,'temporaryFemaleVP':retrieve.temporaryFemaleVP,'permanentMalePGT':retrieve.permanentMalePGT,'permanentFemalePGT':retrieve.permanentFemalePGT,'temporaryMalePGT':retrieve.temporaryMalePGT,'temporaryFemalePGT':retrieve.temporaryFemalePGT,'permanentMaleTGT':retrieve.permanentMaleTGT,
                            'permanentFemaleTGT':retrieve.permanentFemaleTGT,'temporaryMaleTGT':retrieve.temporaryMaleTGT,'temporaryFemaleTGT':retrieve.temporaryFemaleTGT,'permanentMalePRT':retrieve.permanentMalePRT,'permanentFemalePRT':retrieve.permanentFemalePRT,'temporaryMalePRT':retrieve.temporaryMalePRT,'temporaryFemalePRT':retrieve.temporaryFemalePRT,
                            'permanentMaleNTT':retrieve.permanentMaleNTT,'permanentFemaleNTT':retrieve.permanentFemaleNTT,'temporaryMaleNTT':retrieve.temporaryMaleNTT,'temporaryFemaleNTT':retrieve.temporaryFemaleNTT,'permanentUntrainedMale':retrieve.permanentUntrainedMale,'permanentUntrainedFemale':retrieve.permanentUntrainedFemale,'temporaryUntrainedMale':retrieve.temporaryUntrainedMale,
                            'temporaryUntrainedFemale':retrieve.temporaryUntrainedFemale,'permanentMaleLibrarian':retrieve.permanentMaleLibrarian,'permanentFemaleLibrarian':retrieve.permanentFemaleLibrarian,'temporaryMaleLibrarian':retrieve.temporaryMaleLibrarian,'temporaryFemaleLibrarian':retrieve.temporaryFemaleLibrarian,'permanentMaleArts':retrieve.permanentMaleArts,
                            'permanentFemaleArts':retrieve.permanentFemaleArts,'temporaryMaleArts':retrieve.temporaryMaleArts,'temporaryFemaleArts':retrieve.temporaryFemaleArts,'permanentMaleCounsellor':retrieve.permanentMaleCounsellor,'permanentFemaleCounsellor':retrieve.permanentFemaleCounsellor,'temporaryMaleCounsellor':retrieve.temporaryMaleCounsellor,'temporaryFemaleCounsellor':retrieve.temporaryFemaleCounsellor,
                            'permanentMaleLiteracy':retrieve.permanentMaleLiteracy,'permanentFemaleLiteracy':retrieve.permanentFemaleLiteracy,'temporaryMaleliteracy':retrieve.temporaryMaleliteracy,'temporaryFemaleliteracy':retrieve.temporaryFemaleliteracy,'permanentMaleMinister':retrieve.permanentMaleMinister,'permanentFemaleMinister':retrieve.permanentFemaleMinister,'temporaryMaleMinister':retrieve.temporaryMaleMinister,
                            'temporaryFemaleMinister':retrieve.temporaryFemaleMinister,'permanentMaleNurse':retrieve.permanentMaleNurse,'permanentFemaleNurse':retrieve.permanentFemaleNurse,'temporaryMaleNurse':retrieve.temporaryMaleNurse,'temporaryFemaleNurse':retrieve.temporaryFemaleNurse,'permanentMalePT':retrieve.permanentMalePT,'permanentFemalePT':retrieve.permanentFemalePT,'temporaryMalePT':retrieve.temporaryMalePT,'temporaryFemalePT':retrieve.temporaryFemalePT},
            'sclprofile14':{'permanentOfficeManager':retrieve.permanentOfficeManager,'temporaryOfficeManager':retrieve.temporaryOfficeManager,'partTimeOfficeManager':retrieve.partTimeOfficeManager,'permanentOfficeAsst':retrieve.permanentOfficeAsst,'temporaryOfficeAsst':retrieve.temporaryOfficeAsst,'partTimeOfficeAsst':retrieve.partTimeOfficeAsst,'permanentClerk':retrieve.permanentClerk,'temporaryClerk':retrieve.temporaryClerk,'partTimeClerk':retrieve.partTimeClerk,
                            'permanentLabAttendant':retrieve.permanentLabAttendant,'temporaryLabAttendant':retrieve.temporaryLabAttendant,'partTimeLabAttendant':retrieve.partTimeLabAttendant,'permanentAccountant':retrieve.permanentAccountant,'temporaryAccountant':retrieve.temporaryAccountant,'partTimeAccountant':retrieve.partTimeAccountant,'permanentPeon':retrieve.permanentPeon,'temporaryPeon':retrieve.temporaryPeon,'partTimePeon':retrieve.partTimePeon,
                            'permanentOthers':retrieve.permanentOthers,'temporaryOthers':retrieve.temporaryOthers,'partTimeOthers':retrieve.partTimeOthers},
            'sclprofile15':{'noOfCarricularActivity':retrieve.noOfCarricularActivity,'noOfGrps':retrieve.noOfGrps,'noOfCommunity':retrieve.noOfCommunity,'noOfSportsAtSchool':retrieve.noOfSportsAtSchool,'noOfSportsAtZonal':retrieve.noOfSportsAtZonal,'noOfSportsAtDist':retrieve.noOfSportsAtDist,'noOfSportsAtState':retrieve.noOfSportsAtState,'noOfSportsAtNational':retrieve.noOfSportsAtNational,'noOfSportsAtInternational':retrieve.noOfSportsAtInternational,
                            'noOfCompetitionAtSchool':retrieve.noOfCompetitionAtSchool,'noOfCompetitionAtZonal':retrieve.noOfCompetitionAtZonal,'noOfCompetitionAtDist':retrieve.noOfCompetitionAtDist,'noOfCompetitionAtState':retrieve.noOfCompetitionAtState,'noOfCompetitionAtNational':retrieve.noOfCompetitionAtNational,'noOfCompetitionAtInternational':retrieve.noOfCompetitionAtInternational,'noOfSclProgramsAtSchool':retrieve.noOfSclProgramsAtSchool,
                            'noOfSclProgramsAtZonal':retrieve.noOfSclProgramsAtZonal,'noOfSclProgramsAtDist':retrieve.noOfSclProgramsAtDist,'noOfSclProgramsAtState':retrieve.noOfSclProgramsAtState,'noOfSclProgramsAtNational':retrieve.noOfSclProgramsAtNational,'noOfSclProgramsAtInternational':retrieve.noOfSclProgramsAtInternational},
            'sclprofile16':{'academicYearBeginingMonth':retrieve.academicYearBeginingMonth,'academicYearEndingMonth':retrieve.academicYearEndingMonth,'workingDay2021':retrieve.workingDay2021,'workingDay2020':retrieve.workingDay2020,'workingDay2019':retrieve.workingDay2019,'hrsOfAcademic2021':retrieve.hrsOfAcademic2021,'hrsOfAcademic2020':retrieve.hrsOfAcademic2020,'hrsOfAcademic2019':retrieve.hrsOfAcademic2019,'instructionalHrs2021':retrieve.instructionalHrs2021,
                            'instructionalHrs2020':retrieve.instructionalHrs2020,'instructionalHrs2019':retrieve.instructionalHrs2019,'nonInstructuionalWorkingday2021':retrieve.nonInstructuionalWorkingday2021,'nonInstructuionalWorkingday2020':retrieve.nonInstructuionalWorkingday2020,'nonInstructuionalWorkingday2019':retrieve.nonInstructuionalWorkingday2019,'holiday2021':retrieve.holiday2021,'holiday2020':retrieve.holiday2020,'holiday2019':retrieve.holiday2019},
            'sclprofile17':{'noOfSubTeachingPeriod':retrieve.noOfSubTeachingPeriod,'noOfMoralTeachingPeriod':retrieve.noOfMoralTeachingPeriod,'teachingDuration':retrieve.teachingDuration,'noOfClubHrs':retrieve.noOfClubHrs,'fromTimeInSummer':retrieve.fromTimeInSummer,'toTimeInSummer':retrieve.toTimeInSummer,'fromTimeInWinter':retrieve.fromTimeInWinter,'toTimeInWinter':retrieve.toTimeInWinter,'shift':retrieve.shift},
            'sclprofile18':{'scholarship':retrieve.scholarship}
            # 'sclprofile18':{'scholarship': retrow(retrieve.scholarship)}
            }




