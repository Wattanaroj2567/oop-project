import streamlit as st
import time 
import base64


# สร้างข้อมูลซีรีย์เกาหลี
series_data = [
    {"ชื่อภาษาอังกฤษ":"1. Queen of Tears","รายละเอียด":"**ราชินีแห่งน้ำตา** || เรื่องราวความรักระหว่าง ชายหนุ่มผู้ซึ่งเป็นความภาคภูมิใจของหมู่บ้านยงดูรี และเป็นผู้อำนวยการด้านกฎหมายของกลุ่มบริษัท Queens Group ซึ่งได้แต่งงานกับ ทายาทสาวตระกูล Queens Group แม้จะแต่งงานกันมาได้ 3 ปี แล้ว แต่ชีวิตคู่ของพวกเขากำลังเผชิญกับวิกฤตอันน่าหวาดหวั่น","ประเภท":"เมโลดราม่า / โรแมนติก","จำนวนตอนซีรีย์":"16 ตอน","วันเริ่มออกอากาศ":" 9 มีนาคม 2024","ช่องทางการรับชม":"Netfilx ","ตัวอย่างซีรีย์":"https://youtu.be/xHT9kcaUEGY","รูป":"images/Queen of Tears.jpg"},
    {"ชื่อภาษาอังกฤษ":"2. The Impossible Heir","รายละเอียด":"เรื่องราวการพบกันของ คน 3 คน ที่ต่างเป็นผู้เล่นนอกสนาม ที่ต่อสู้ดิ้นรนเพื่อไต่เต้าสู่จุดสูงสุดของตระกูลแชบอลที่ยิ่งใหญ่ที่สุดในเกาหลี โดยติดตามชีวิตของ ฮันแทโอ (**รับบทโดย อีแจอุค**) ชายหนุ่มฉลาดหลักแหลมที่ถูกตีตราว่าเป็นลูกฆาตกร ได้มาพบกับ คังอินฮา (**รับบทโดย อีจุนยอง**) ลูกชายนอกสมรสของตระกูลแชบอล และพวกเขาได้ร่วมมือกันเพื่อให้ได้มาซึ่งอำนาจโดยชอบธรรมในตระกูล ขณะที่กำลังมุ่งหน้าสู่เป้าหมาย ทั้งมิตรภาพและแผนการของพวกเขา ก็สั่นคลอน เมื่อได้มี นาฮเยวอน (**รับบทโดย ฮงซูจู**) หญิงสาวผู้มีความทะเยอทะยานไม่แพ้กันเข้ามาพัวพัน ขณะที่เรื่องราวดำเนินไป ใยแมงมุมแห่งคำโกหก การทรยศ และความทะเยอทะยานได้ถูกถักทออย่างแน่นขึ้นเรื่อย ๆ","ประเภท":"ดราม่า / เข้มข้น","จำนวนตอนซีรีย์":"12 ตอน","วันเริ่มออกอากาศ":"28 กุมภาพันธ์ 2024","ช่องทางการรับชม":"Disney+ Hotstar","ตัวอย่างซีรีย์":"https://youtu.be/iOajWK2yZfE","รูป":"images/The Impossible Heir.jpg"},
    {"ชื่อภาษาอังกฤษ":"3. Doctor Slump","รายละเอียด":"**หัวใจหมอไม่มอดไหม้** || เพื่อนสมัยเรียนที่ทั้งคู่ต่างประสบความสำเร็จในหน้าที่การงานในอาชีพแพทย์ แต่กลับเผชิญช่วงเวลาที่ตกต่ำที่สุดในชีวิต การได้กลับมาเจอกันในจุดสำคัญของชีวิตทำให้ทั้งคู่ช่วยเยียวยาหัวใจซึ่งกันและกัน","ประเภท":"ดราม่า / โรแมนติก / การแพทย์ / คอเมดี้","จำนวนตอนซีรีย์":"16 ตอน","วันเริ่มออกอากาศ":" 27 มกราคม 2024","ช่องทางการรับชม":"Netfilx ","ตัวอย่างซีรีย์":"https://youtu.be/oGyWHLCf4NQ","รูป":"images/Doctor Slump.jpg"},
    {"ชื่อภาษาอังกฤษ":"4. Flex X Cop","รายละเอียด":"ทายาทตระกูลมหาเศรษฐีรุ่นที่ 3 หนุ่มเสเพลชอบปาร์ตี้ แต่จับพลัดจับผลูเข้าไปเกี่ยวพันกับคดีหนึ่ง จนต้องกลายมาเป็นตำรวจสายสืบในหน่วยปราบปรามอาชญากรรม","ประเภท":"แอคชั่น / ลึกลับ/ คอเมดี้ / โรแมนติก","จำนวนตอนซีรีย์":"16 ตอน","วันเริ่มออกอากาศ":" 26 มกราคม 2024","ช่องทางการรับชม":"Disney+ Hotstar ","ตัวอย่างซีรีย์":"https://youtu.be/78pJ3-hSEwM","รูป":"images/Flex X Cop.jpg"},
    {"ชื่อภาษาอังกฤษ":"5. Marry My Husband","รายละเอียด":"**สามีคนนี้แจกฟรีให้เธอ** || หญิงสาวที่ป่วยหนักและรู้ความจริงว่าสามีกับเพื่อนรักของเธอแอบคบชู้กัน จนทำให้เธอต้องจากโลกนี้ไปก่อนเวลาอันควร แต่แล้วเธอได้ข้ามเวลากลับไปเมื่อสิบปีก่อนหน้า  แผนการล้างแค้นของเธอจึงเริ่มต้นขึ้น","ประเภท":"ดราม่า / โรแมนติก / แฟนตาซี","จำนวนตอนซีรีย์":"16 ตอน","วันเริ่มออกอากาศ":"1 มกราคม 2024","ช่องทางการรับชม":"Prime Video","ตัวอย่างซีรีย์":"https://youtu.be/ufSwMGPZDH4","รูป":"images/Marry My Husband.jpg"},
    {"ชื่อภาษาอังกฤษ":"6. Captivating The King ","รายละเอียด":"**เสน่ห์ร้ายบัลลังก์ลวง**|| กษัตริย์ที่กำลังเผชิญกับการต่อสู้แย่งชิงอำนาจทางการเมือง หญิงสาวผู้พยายามเกลี้ยกล่อมและหลอกล่อองค์กษัตริย์ เพื่อแก้แค้น แต่เธอกลับถูกล่อลวงแทน","ประเภท":"ดราม่า / โรแมนติก / ย้อนยุค","จำนวนตอนซีรีย์":"16 ตอน","วันเริ่มออกอากาศ":"  21 มกราคม 2024","ช่องทางการรับชม":" Netfilx","ตัวอย่างซีรีย์":"https://youtu.be/_1t7mqiqtkk","รูป":"images/Captivating The King.jpg"},
    {"ชื่อภาษาอังกฤษ":"7. Gyeongseong Creature","รายละเอียด":"**สัตว์สยองกยองซอง ภาค 2** || ซีรีย์แนวสัตว์ประหลาดสุดระทึกขวัญ เรื่องราวภาคต่อของกลุ่มคนที่ลุกขึ้นต่อกรกับอสุรกายที่ถือกำเนิดจากความโลภของมนุษย์","ประเภท":"แอคชั่น / ระทึกขวัญ / ไซไฟ","จำนวนตอนซีรีย์":"10 ตอน","วันเริ่มออกอากาศ":" ซีซั่นที่ 1 แบ่งสตรีมครั้งแรกเป็น 2 พาร์ท : 22 ธันวาคม 2566 สตรีมได้ 7 ตอนและ 5 มกราคม 2567 สตรีมได้อีก 3 ตอน |||  ซีซั่น 2 ควอเตอร์ที่ 3 ปี 2567","ช่องทางการรับชม":"Netflix","ตัวอย่างซีรีย์":"https://youtu.be/ATEin6-V0oU?si=0W7piMhP7mUuTHOn","รูป":"images/Gyeongseong Creature.jpg"},
    {"ชื่อภาษาอังกฤษ":"8. A Shop For Killers","รายละเอียด":"หญิงสาวได้รับการเลี้ยงดูจากคุณอาตั้งแต่เด็ก แต่แล้วคุณอาก็จากไปอย่างกะทันหัน ทำให้เธอต้องรับหน้าที่ดูแลธุรกิจที่เต็มไปด้วยปริศนาต่อ แถมเธอยังตกเป็นเป้าของมือสังหารที่มาตามคร่าชีวิตอีกด้วย","ประเภท":"ดราม่า / ลึกลับ / แอคชั่น / ระทึกขวัญ","จำนวนตอนซีรีย์":"8 ตอน","วันเริ่มออกอากาศ":" 17 มกราคม 2024","ช่องทางการรับชม":" Disney+ Hotstar","ตัวอย่างซีรีย์":"https://youtu.be/FBbFtJ3-HtM","รูป":"images/A Shop For Killers.jpg"},
    {"ชื่อภาษาอังกฤษ":"9. A Killer Paradox","รายละเอียด":"**หน้ากากความยุติธรรม** || เมื่อหนุ่มนักศึกษา เผลอไปฆ่าคนตาย เรื่องก็ยิ่งบานปลาย เพราะมีตำรวจมือดีมาพัวพัน","ประเภท":"อาชญากรรม / คอเมดี้ / ระทึกขวัญ","จำนวนตอนซีรีย์":"8 ตอน","วันเริ่มออกอากาศ":" 1 มกราคม 2024","ช่องทางการรับชม":"Netfilx ","ตัวอย่างซีรีย์":"https://youtu.be/iaTGzZ-lYlw","รูป":"images/A Killer Paradox.jpg"},
    {"ชื่อภาษาอังกฤษ":"10. Squid Game season 2","รายละเอียด":"**สควิดเกม เล่นลุ้นตาย ซีซั่น 2** ||การกลับมาคราวนี้รับรองว่าโหดและเดือดมากขึ้นกว่าเดิม เพราะเปิดเผยออกมาแล้วว่าผู้บงการ ฮวังดงฮยอก เป็นผู้ควบคุมเกมในซีซั่นนี้ โดยเนื้อหาจะดำเนินต่อจากเหตุการณ์ตอนจบของซีซั่นแรก","ประเภท":"ดราม่า / ระทึกขวัญ / ลึกลับ / แอคชั่น","จำนวนตอนซีรีย์":"6 ตอน","วันเริ่มออกอากาศ":"ปลายปี 2024","ช่องทางการรับชม":"Netfilx","ตัวอย่างซีรีย์":"https://youtu.be/sLJ5bDB1Uj8","รูป":"images/Squid Game 2.jpg"},
              ]
#สร้างหน้า Tab
tab1, tab2 ,tab3 = st.tabs([':house: หน้าหลัก', ':balloon: มาแรง',':gear: เพิ่มเติม'])
with tab1:
    st.header("코리안 시리즈 Korean Series:tv:")
    st.subheader(":wave:ยินดีต้อนรับเข้าสู่เว็บไซต์แนะนำซีรีย์เกาหลี")
    
   # แสดงช่องค้นหาซีรีย์ในแท็บ "หน้าหลัก"
    search_query = st.text_input(":mag:ค้นหาซีรีย์ที่ต้องการ", "")
   #ลูกเล่น
    def snow_1():
        msg = st.toast('Loading...')
        time.sleep(1)
        msg.toast('Snow...')
        time.sleep(1)
        msg.toast('Ready!', icon = "☃️")
        st.snow()
    
    if st.button('คลิก:snowflake:เพื่อเล่น'):
       snow_1()
       
    # ถ้ามีการค้นหา
    if search_query:
        filtered_series = [series for series in series_data if search_query.lower() in series["ชื่อภาษาอังกฤษ"].lower()]
        if filtered_series:
            for series in filtered_series:
                col1, col2,  = st.columns([1, 2])
                with col1:
                    st.image(series["รูป"],use_column_width=True)  
                with col2:
                    st.subheader(series["ชื่อภาษาอังกฤษ"])
                    st.write(series["รายละเอียด"])
                    st.write("**ประเภท:**" , series["ประเภท"])
                    st.write("**จำนวนตอนซีรีย์:**" , series["จำนวนตอนซีรีย์"])
                    st.write("**วันเริ่มออกอากาศ:**" , series["วันเริ่มออกอากาศ"])
                    st.write("**ช่องทางการรับชม:**", series["ช่องทางการรับชม"])
                    st.write("**ตัวอย่างซีรีย์:**")
                    
                    # ตัวกำหนดเรียกลิงค์เข้าเว็บ Youtube
                    VIDEO_URL = series["ตัวอย่างซีรีย์"]
                    st.video(VIDEO_URL)
                    st.header(" ") #เว้นระหว่างความสูงส่วนต่อของเรื่อง

        else:
            st.warning("ขออภัยครับ:pray:ไม่พบข้อมูลซีรีย์ที่คุณค้นหา")

    st.write('**:bulb:รายชื่อซีรีย์ที่น่าค้นหามากที่สุด**')
    st.text("=> 1. Queen of Tears")
    st.text("=> 2. Marry My Husband") 
    st.text("=> 3. Gyeongseong Creature") 
    st.text("=> 4. Captivating The King") 
    st.text("=> 5. A Shop For Killers")
    st.image('./images/Koreanseries.jpg',caption='ภาพรวมของซีรีย์ทั้งหมดที่ถูกคัดสรรมาโดยเฉพาะ')

    #การกำกับปีที่ทำ
    st.write("Copyright  :copyright: 2024 by OOP-Project **Wattanaroj Butdee** ")

with tab2:
    st.header("**:clapper:10 อันดับมาแรงในปีนี้ 2024:thumbsup:**")
    for series in series_data:
        col1, col2,  = st.columns([1, 2])
        with col1:
            st.image(series["รูป"],use_column_width=True)
        with col2:
             st.subheader(series["ชื่อภาษาอังกฤษ"])
             st.write(series["รายละเอียด"])
             st.write("**ประเภท:**" , series["ประเภท"])
             st.write("**จำนวนตอนซีรีย์:**" , series["จำนวนตอนซีรีย์"])
             st.write("**วันเริ่มออกอากาศ:**" , series["วันเริ่มออกอากาศ"])
             st.write("**ช่องทางการรับชม:**", series["ช่องทางการรับชม"])
             st.write("**ตัวอย่างซีรีย์**")
             
             # ตัวกำหนดเรียกลิงค์เข้าเว็บ Youtube
             VIDEO_URL = series["ตัวอย่างซีรีย์"]
             st.video(VIDEO_URL)
             st.header(" ") #เว้นระหว่างความสูงส่วนต่อของเรื่อง
#การกำกับปีที่ทำ
    st.write("Copyright  :copyright: 2024 by OOP-Project **Wattanaroj Butdee** ")

with tab3:
    st.subheader("การติดต่อ:calling:")
    st.write(" > :point_right: ท่านที่ต้องการติดต่อสามารถติดต่อผู้พัฒนาเว็บไซต์ที่สร้างชื่อเว็บนี้ของ Streamlit ได้โดยตรง")
    #Emoji ชี้ลง
    #st.write(":point_down::point_down:")
    st.markdown(":envelope:**Email** : wattanaroj.bu.66@ubu.ac.th")
    #Logo
    image_github = "images/Other/github.png"
    github_usl = "https://github.com/wattanaroj2567"
    image_googleform = "images/Other/googleform.png"
    google_form_usl = "https://forms.gle/sbUCwK2GhNWWRGg28"

    with open(image_github ,"rb") as f:
        image_data = f.read()
    image_base6401 = base64.b64encode(image_data).decode()

    
    with open(image_googleform,"rb") as f:
        image_data = f.read()
    image_base6402 = base64.b64encode(image_data).decode()
    

    st.markdown(f'<a href="{github_usl}" target="_blank"><img src="data:image/jpeg;base64,{image_base6401}" alt="Github" width="60"></a>',unsafe_allow_html=True)
    st.write("ช่องทางการติดตาม :  Github [ **Click Image**:pick: ]")
    st.write("") #เว้นระยะห่าง
    st.markdown(f'<a href="{google_form_usl}" target="_blank"><img src="data:image/jpeg;base64,{image_base6402}" alt="Goolge Form" width="50"></a>',unsafe_allow_html=True)
    st.write("แบบสอบถาม [ **Click Image**:pick: ]")

    #อ้างอิง
    st.subheader("แหล่งนำเข้าข้อมูลซีรีย์:inbox_tray:")
    st.write("**Mushroomtravel** :link: https://www.mushroomtravel.com/page/korean-series-first-half-year-2018/")
    st.write("**Korseries** :link: https://www.korseries.com/")

    #การกำกับปีที่ทำ
    st.write("Copyright  :copyright: 2024 by OOP-Project **Wattanaroj Butdee** ")

