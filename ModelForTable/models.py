from sqlalchemy import Column, Integer,String,Date,BigInteger,TIME,Boolean,ForeignKey
from DatabaseFile.database import Base

class register(Base):
    __tablename__ = "register"
    id = Column(Integer, primary_key = True, nullable=False, autoincrement=True)
    firstname = Column(String, nullable =False)
    lastname = Column(String,nullable = False)
    phone = Column(BigInteger, nullable =False)
    email = Column(String,nullable = False, unique= True)
    dob = Column(Date, nullable = False)
    gender = Column(String,nullable = False)
    pwd = Column(String,nullable = False)

class Scl_Profile(Base):
    __tablename__ = "scl_profile"
    owner_id = Column(Integer,ForeignKey("register.id",ondelete="CASCADE"), nullable = False)
    id = Column(Integer, primary_key = True, nullable=False, autoincrement=True)
    inst_name = Column(String, nullable =False)
    postal = Column(String,nullable = False)
    dis = Column(String,nullable = False)
    state = Column(String,nullable = False)
    city = Column(String, nullable = False)
    pin = Column(BigInteger,nullable = False)
    url = Column(String,nullable = False)
    off_email = Column(String,nullable = False)
    off_phone = Column(BigInteger,nullable = False)
    scl_loc = Column(String,nullable = False)
    est_year = Column(BigInteger,nullable = False)
    medium = Column(String,nullable = False)
    nat_affiliation = Column(String,nullable = False)
    scl_level = Column(String,nullable = False)
    gen = Column(String,nullable = False)
    girls = Column(Integer,nullable = False)
    boys = Column(Integer,nullable = False)
    total_stu = Column(Integer,nullable = False)
    teaching_staff= Column(Integer,nullable = False)
    non_teaching = Column(Integer,nullable = False)
    cors_name = Column(String,nullable = False)
    cors_mobile = Column(BigInteger,nullable = False)
    cors_email= Column(String,nullable = False)
    prin_name = Column(String,nullable = False)
    prin_phone = Column(BigInteger,nullable = False)
    prin_email= Column(String,nullable = False)
    prin_mobile = Column(BigInteger,nullable = False)
    reg_govt = Column(String,nullable = False)
    board_name = Column(String,nullable = False) 
    affli_no = Column(BigInteger,nullable = False)
    affili_year = Column(Integer,nullable = False)
    per_temp = Column(String,nullable = False)
    cond = Column(BigInteger,nullable = False)
    minor_sta_cer = Column(String,nullable = False)
    christian = Column(Integer,nullable = False)
    hindu = Column(Integer,nullable = False)
    muslim= Column(Integer,nullable = False)
    others= Column(Integer,nullable = False)
    non_believe= Column(Integer,nullable = False)
    fire= Column(String,nullable = False)
    sanitation= Column(String,nullable = False)
    building= Column(String,nullable = False)
    scl_owned= Column(String,nullable = False)
    trust_name= Column(String,nullable = False)
    registered= Column(String,nullable = False)
    act= Column(String,nullable = False)
    reg_year= Column(Integer,nullable = False)
    reg_no= Column(Integer,nullable = False)
    reg_validity= Column(Integer,nullable = False)
    president_name = Column(String,nullable = False)
    designation= Column(String,nullable = False)
    address= Column(String,nullable = False)
    president_phone= Column(BigInteger,nullable = False)
    president_email= Column(String,nullable = False)
    governing= Column(String,nullable = False)
    members= Column(Integer,nullable = False)
    mem_tenure= Column(Integer,nullable = False)
    EPCC = Column(String,nullable = False)
    EPCC_mem= Column(Integer,nullable = False)
    EPCC_tenure= Column(Integer,nullable = False)
    par_techer= Column(String,nullable = False)
    par_teacher_mem= Column(Integer,nullable = False)
    par_techer_tenure= Column(Integer,nullable = False)
    stud = Column(String,nullable = False)
    stud_mem= Column(Integer,nullable = False)
    stud_tenure= Column(Integer,nullable = False)
    general= Column(String,nullable = False)
    scl_manage_commi= Column(String,nullable = False)
    constitute_commi= Column(String,nullable = False)
    constitute_mem= Column(Integer,nullable = False)
    constitute_tenure= Column(Integer,nullable = False)
    scl_location= Column(String,nullable = False)
    area= Column(String,nullable = False)
    built_area= Column(String,nullable = False)
    play_area= Column(String,nullable = False)
    no_building= Column(Integer,nullable = False)
    provision= Column(String,nullable = False)
    no_staircase= Column(Integer,nullable = False)
    no_lifts= Column(Integer,nullable = False)
    class_room= Column(Integer,nullable = False)
    staff_room= Column(Integer,nullable = False)
    physics_lab= Column(Integer,nullable = False)
    chemistry_lab= Column(Integer,nullable = False)
    bio_lab= Column(Integer,nullable = False)
    math_lab= Column(Integer,nullable = False)
    comp_lab= Column(Integer,nullable = False)
    lang_lab= Column(Integer,nullable = False)
    home_lab= Column(Integer,nullable = False)
    library= Column(Integer,nullable = False)
    auditorium= Column(Integer,nullable = False)
    counselor_room= Column(Integer,nullable = False)
    visitor_parlor= Column(Integer,nullable = False)
    prayer_room= Column(Integer,nullable = False)
    sick_room= Column(Integer,nullable = False)
    canteen= Column(Integer,nullable = False)
    security_room= Column(Integer,nullable = False)
    other_room= Column(Integer,nullable = False)
    staff_toilet= Column(Integer,nullable = False)
    stu_toilet= Column(Integer,nullable = False)
    room= Column(Integer,nullable = False)
    spl_need= Column(String,nullable = False)
    staff_spl_need= Column(String,nullable = False)
    boundary_wall= Column(String,nullable = False)
    wall_status= Column(String,nullable = False)
    cctv= Column(String,nullable = False)
    data_saved= Column(String,nullable = False)
    no_camera= Column(Integer,nullable = False)
    male_guard= Column(String,nullable = False)
    no_male_guard= Column(Integer,nullable = False)
    female_guard= Column(String,nullable = False)
    no_female_guard= Column(String,nullable = False)
    water_facility= Column(String,nullable = False)
    drainage_facility= Column(String,nullable = False)
    midday= Column(String,nullable = False)
    no_bus= Column(Integer,nullable = False)
    gps_camera= Column(Integer,nullable = False)
    lady_attendantor= Column(Integer,nullable = False)
    first_aid= Column(Integer,nullable = False)
    drinking_water= Column(Integer,nullable = False)
    bus_sub_contract= Column(Integer,nullable = False)
    bus_pass= Column(String,nullable = False)
    free_transport= Column(String,nullable = False)
    lib_open= Column(TIME,nullable = False)
    lib_close= Column(TIME,nullable = False)
    no_book= Column(Integer,nullable = False)
    no_magazine= Column(Integer,nullable = False)
    no_newspaper= Column(Integer,nullable = False)
    no_ebook= Column(Integer,nullable = False)
    online_access= Column(String,nullable = False)
    sep_lib= Column(String,nullable = False)
    remedial_teaching= Column(String,nullable = False)
    multimedia1= Column(Boolean ,nullable = False)
    multimedia2= Column(Boolean ,nullable = False)
    multimedia3= Column(Boolean ,nullable = False)
    multimedia4= Column(Boolean ,nullable = False)
    multimedia5= Column(Boolean ,nullable = False)
    prin_per_male= Column(Integer,nullable = False)
    prin_per_female= Column(Integer,nullable = False)
    prin_tem_male= Column(Integer,nullable = False)
    prin_tem_female= Column(Integer,nullable = False)
    vp_per_male= Column(Integer,nullable = False)
    vp_per_female= Column(Integer,nullable = False)
    vp_tem_male= Column(Integer,nullable = False)
    vp_tem_female= Column(Integer,nullable = False)
    pgt_per_male= Column(Integer,nullable = False)
    pgt_per_female= Column(Integer,nullable = False)
    pgt_tem_male= Column(Integer,nullable = False)
    pgt_tem_female= Column(Integer,nullable = False)
    tgt_per_male= Column(Integer,nullable = False)
    tgt_per_female= Column(Integer,nullable = False)
    tgt_tem_male= Column(Integer,nullable = False)
    tgt_tem_female= Column(Integer,nullable = False)
    prt_per_male= Column(Integer,nullable = False)
    prt_per_female= Column(Integer,nullable = False)
    prt_tem_male= Column(Integer,nullable = False)
    prt_tem_female= Column(Integer,nullable = False)
    ntt_per_male= Column(Integer,nullable = False)
    ntt_per_female= Column(Integer,nullable = False)
    ntt_tem_male= Column(Integer,nullable = False)
    ntt_tem_female= Column(Integer,nullable = False)
    untrained_per_male= Column(Integer,nullable = False)
    untrained_per_female= Column(Integer,nullable = False)
    untrained_tem_male= Column(Integer,nullable = False)
    untrained_tem_female= Column(Integer,nullable = False)
    lib_per_male= Column(Integer,nullable = False)
    lib_per_female= Column(Integer,nullable = False)
    lib_tem_male= Column(Integer,nullable = False)
    lib_tem_female= Column(Integer,nullable = False)
    art_per_male= Column(Integer,nullable = False)
    art_per_female= Column(Integer,nullable = False)
    art_tem_male= Column(Integer,nullable = False)
    art_tem_female= Column(Integer,nullable = False)
    counsellor_per_male= Column(Integer,nullable = False)
    counsellor_per_female= Column(Integer,nullable = False)
    counsellor_tem_male= Column(Integer,nullable = False)
    counsellor_tem_female= Column(Integer,nullable = False)
    lit_per_male= Column(Integer,nullable = False)
    lit_per_female= Column(Integer,nullable = False)
    lit_tem_male= Column(Integer,nullable = False)
    lit_tem_female= Column(Integer,nullable = False)
    faith_per_male= Column(Integer,nullable = False)
    faith_per_female= Column(Integer,nullable = False)
    faith_tem_male= Column(Integer,nullable = False)
    faith_tem_female= Column(Integer,nullable = False)
    nurse_per_male= Column(Integer,nullable = False)
    nurse_per_female= Column(Integer,nullable = False)
    nurse_tem_male= Column(Integer,nullable = False)
    nurse_tem_female= Column(Integer,nullable = False)
    pt_per_male= Column(Integer,nullable = False)
    pt_per_female= Column(Integer,nullable = False)
    pt_tem_male= Column(Integer,nullable = False)
    pt_tem_female= Column(Integer,nullable = False)
    off_manager_per= Column(Integer,nullable = False)
    off_manager_tem= Column(Integer,nullable = False)
    off_manager_part= Column(Integer,nullable = False)
    off_asst_per= Column(Integer,nullable = False)
    off_asst_tem= Column(Integer,nullable = False)
    off_asst_part= Column(Integer,nullable = False)
    clerk_per= Column(Integer,nullable = False)
    clerk_tem= Column(Integer,nullable = False)
    clerk_part= Column(Integer,nullable = False)
    lab_per= Column(Integer,nullable = False)
    lab_tem= Column(Integer,nullable = False)
    lab_part= Column(Integer,nullable = False)
    accountant_per= Column(Integer,nullable = False)
    accountant_tem= Column(Integer,nullable = False)
    accountant_part= Column(Integer,nullable = False)
    peon_per= Column(Integer,nullable = False)
    peon_tem= Column(Integer,nullable = False)
    peon_part= Column(Integer,nullable = False)
    other_per= Column(Integer,nullable = False)
    other_tem= Column(Integer,nullable = False)
    other_part= Column(Integer,nullable = False)
    no_curri_act= Column(Integer,nullable = False)
    no_grp= Column(Integer,nullable = False)
    no_community= Column(Integer,nullable = False)
    scl= Column(Integer,nullable = False)
    zonal= Column(Integer,nullable = False)
    dist= Column(Integer,nullable = False)
    stat= Column(Integer,nullable = False)
    national= Column(Integer,nullable = False)
    international= Column(Integer,nullable = False)
    c_scl= Column(Integer,nullable = False)
    c_zonal= Column(Integer,nullable = False)
    c_dist= Column(Integer,nullable = False)
    c_stat= Column(Integer,nullable = False)
    c_national= Column(Integer,nullable = False)
    c_international= Column(Integer,nullable = False)
    inter_scl= Column(Integer,nullable = False)
    inter_zonal= Column(Integer,nullable = False)
    inter_dist= Column(Integer,nullable = False)
    inter_stat= Column(Integer,nullable = False)
    inter_national= Column(Integer,nullable = False)
    inter_international= Column(Integer,nullable = False)
    ac_begin_mon= Column(String,nullable = False)
    ac_end_mon= Column(String,nullable = False)
    working_day_21= Column(Integer,nullable = False)
    working_day_20= Column(Integer,nullable = False)
    working_day_19= Column(Integer,nullable = False)
    hrs_21= Column(Integer,nullable = False)
    hrs_20= Column(Integer,nullable = False)
    hrs_19= Column(Integer,nullable = False)
    instruct_hrs_21= Column(Integer,nullable = False)
    instruct_hrs_20= Column(Integer,nullable = False)
    instruct_hrs_19= Column(Integer,nullable = False)
    non_instruct_hrs_21= Column(Integer,nullable = False)
    non_instruct_hrs_20= Column(Integer,nullable = False)
    non_instruct_hrs_19= Column(Integer,nullable = False)
    holiday_21= Column(Integer,nullable = False)
    holiday_20= Column(Integer,nullable = False)
    holiday_19= Column(Integer,nullable = False)
    sub_teaching_week= Column(Integer,nullable = False)
    moral_week= Column(Integer,nullable = False)
    teaching_duration= Column(Integer,nullable = False)
    hrs_club= Column(Integer,nullable = False)
    scl_tim_sum_from= Column(TIME,nullable = False)
    scl_tim_sum_to= Column(TIME,nullable = False)
    scl_tim_win_from= Column(TIME,nullable = False)
    scl_tim_win_to= Column(TIME,nullable = False)
    shift= Column(String,nullable = False)
    # scholarship = Column(String, nullable = True)


    






    
   

    




