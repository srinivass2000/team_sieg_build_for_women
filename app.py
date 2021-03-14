from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('investment_pred_model.pkl', 'rb'))
ct = pickle.load(open('investment_pred_model_ct.pkl', 'rb'))
model2 = pickle.load(open('model2.pkl', 'rb'))
ct2 = pickle.load(open('model2_ct.pkl', 'rb'))


# Flask constructor 
app = Flask(__name__)    


@app.route('/')
def main():
    name1 = "Falguni Nayar"
    content1= """ Falguni was an investment banker who turned into an entrepreneur. She launched Nykaa in 2012. Nykaa is worth $473million and very soon we can see them in unicorn list."""
    exp1= "Founder of Nykaa"
    name2 = "Upasana Taku" 
    content2= """Upasana launched MobiKwik in 2009 with her husband Bipin Preet Singh. In 2013, RBI authorized the company’s use of the Mobikwik wallet, and in May 2016 company started giving small loans to its consumers as part of their services. As of today, they have many known clients like Uber, IRCTC, Zomato, Bluedart."""
    exp2= "Founder of Mobikwik"
    name3 = "Sabina Chopra"
    content3= """ Yatra.com is a public listed company. In 2019, it was acquired by Ebix, a US-based company for $338 million. """
    exp3= "Founder of Yatra"
    return render_template('index.html',name1=name1,name2=name2,name3=name3,content1=content1,content2=content2,content3=content3,exp1=exp1,exp2=exp2,exp3=exp3)

@app.route('/register')
def register():
    return render_template('form.html')

@app.route('/investment')
def invest():
    return render_template('investment.html')
    
@app.route('/salary')
def salary():
    return render_template('salary.html')

@app.route('/joinus')
def joinus():
    return render_template('joining.html')

@app.route('/ads')
def ads():
    return render_template('form.html')




@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form.get("a") 
    print(data1)
    data2 = request.form.get("b") 
    print(data2)
    data3 = request.form.get("c")
    print(data3)
    arr = np.array([[data1, data2, data3]])
    arre=ct.transform(arr)
    pred = model.predict(arre)
    print(pred)
    # print(type(pred))
    print(pred[0])
    p=round(pred[0],2)
    print(p)
    k="Looks like you will need a investment of"
    return render_template('after.html',p=p*4000,k=k);

@app.route('/predict2', methods=['POST'])
def home2():
    data1 = request.form.get("a") 
    data2 = request.form.get("b") 
    data3 = request.form.get("c")
    data4=request.form.get("d")
    arr = np.array([[data1, data2, data3,data4]])
    arre=ct2.transform(arr)
    pred = model2.predict(arre)
    print(pred)
    # print(type(pred))
    print(pred[0])
    p=round(pred[0],2)
    print(p)
    print(p*7)
    p=round(p*7,1)
    k="Your estimated Annual salary is :"
    return render_template('after.html',p=p,k=k)



@app.route('/reg', methods=['POST'])
def reg():
    name = request.form.get("name")  
    email = request.form.get("email")  
    return render_template("success.html",name=name,email=email) 


@app.route('/vlcc')
def vlcc():
    name = "Vandana Luthra"  
    title="Vandana Luthra – Founder of VLCC"
    age = "49"  
    edu="Polytechnic for Women in New Delhi"
    exp="homemaker"
    profile="vlcc.jpg"
    content="""Who doesn't know VLCC?

It is a beauty and wellness giant and has its presence in 11 countries across Asia, Africa and the GCC (Gulf Cooperation Council). It is widely recognized for its weight loss solutions and therapeutic approach to beauty treatments. One stop-solution for every beauty related query, VLCC has a staff strength of over 4,000 professionals, including medical doctors, nutritionists, physiotherapists and cosmetologists, and having served over five million consumers (including repeat consumers).

The founder, Mrs. Vandana Luthra, is awarded the Padma Shri in 2013 for her contribution and is listed as the 33rd most powerful woman in business in India by Fortune India, in 2015. Along with these accolades, she was also appointed as the Chairperson of the Beauty & Wellness Sector Skill Council by the Indian government. Furthermore, she is a General Body Member of the New Delhi-based Morarji Desai National Institute of Yoga. The Steering Committee and the Sub-Committee formed by India’s Ministry of Skill Development & Entrepreneurship on the Pradhan Mantri Kaushal Vikas Yojana also has her as an active member.

But nothing happens in one day. Vandana and VLCC didn't happen overnight. A homemaker initially, Vandana started her journey in 1989 when the first of her two daughters was only 3 years-old and today a grandmother to three kids, Vandana still lives her dream.

Remembering her days of struggle she says, “When I started, there were hardly any women entrepreneurs in India. It was a male-dominated environment. I had to face a lot of criticism, a lot of people tried to ensure that I did not succeed and grow. The only thing I believed in was that my concept was unique, unusual and it was being introduced in India for the first time.

It took me a good five to six years to convince the medical fraternity to understand that wellness was a larger domain and it required the collaboration of beauty, health and fitness experts; in other words a cosmetologist, a nutritionist, and a doctor. Eventually, I did manage to convince them."""
    
    return render_template("story.html",name=name,title=title,age=age,edu=edu,exp=exp,content=content,profile=profile)
  
@app.route('/limeroad')
def limeroad():
    name = "Suchi Mukherjee"  
    title="Suchi Mukherjee – Founder & CEO of Limeroad"
    age = " 45"  
    edu=" Economics and Finance from London School of Economics"
    exp="Lehman Brothers Inc, VirginMedia, eBay, Skype, Gumtree"
    profile="limeroad.jpg"
    content= """Suchi, a woman of substance, always envisioned of building and growing businesses that are focused on simple yet in-demand consumer products. It is said, that the idea of Limeroad came to her, while she was on her Maternity leave.

She embarked on the journey of making Limeroad, in 2012 along with Manish Saksena, Ankush Mehra, and Prashant Malik. The company has now raised a funding of $20 Million from Lightspeed venture partners, Matrix Partners and Tiger Global. Limeroad has a strong team of 200+ IIT-techies to NIFT-design geeks. It has 1.5 million scrapbooks posted by users so far, and 100,000 scrapbooks made per day. Their Gross Merchandise Value (GMV) has also grown by a massive 600% since their launch.

If you want to earn money online, read our Hindi article on it. Click Here!!

Nevertheless, Suchi and her associates had to face numerous challenges like,  finding the right people to build a solid team which has a combination of skill and can-do attitude, getting the right kind of infrastructure. Amongst the N-number of hurdles like complex bank processes, net gateways for the payment methods and refunds, delivering unique products at an economical price, the most troublesome part for Suchi and her team was to partner with vendors to ensure a sustained stream of products. The existing eco-system for the professionally trained vendors is a daunting task to date. But as she was determined to achieve what she had dreamt of, nothing could hold her back."""
    
    return render_template("story.html",name=name,title=title,age=age,edu=edu,exp=exp,content=content,profile=profile)

@app.route('/zivame')
def zivame():
    name = "Richa Kar"  
    title="Richa Kar – Co-founder of Zivame"
    age = "30"  
    edu="Narsee Monjee Institute of Management Studies"
    exp=" SAP, Spencer’s Retail Ltd."
    profile="zimave.jpg"
    content= """Richa is the proud founder of online lingerie store Zivame, which is derived from a Hebrew word ‘Ziva’ which means radiance and Zivame stands for a ‘radiant me’. She has practically changed the way women used to think and buy their inner wears. Zivame has been successful in educating Indian women across the country about intimate wear.

Richa, who bravely removed the shyness from lingerie and added a fashion element to it, grew up in Jamshedpur and completed her engineering from BITS Pilani. She worked briefly in the IT industry and later acquired Masters’ degree from Narsee Monjee Institute of Management Studies in 2007. After that, she worked with a retailer and global technology company.

So what made her come across this unique idea of selling female inner wears, online, that too in a conservative country like India. When asked, she says, “It was around March when I realized that there is a high surge in orders during Valentine’s Day sales period. Almost a quarter of the lingerie maker’s sales were generated online”.

Once the idea struck her, there was no looking back. With an initial investment of rupees 30 Lakhs, from friends and family, Zivame.com went online. She did face a lot of apprehension and discomfort while explaining her business idea to her family and others. But she was firm to rise above all, which she certainly did."""
    return render_template("story.html",name=name,title=title,age=age,edu=edu,exp=exp,content=content,profile=profile)


@app.route('/govt1')
def govt1():
    name = "SUMMARY Access to 3000 MSME Women Entrepreneurs to GeM"  
    title="Access to 3000 MSME Women Entrepreneurs to GeM"
    pic="govt1.png"
    scheme="The Government Scheme for Women"
    content= """The International Women’s Day, the Government rolled out a new initiative to help over 3K women entrepreneurs from the MSME sector to sell on the state-run Government e-marketplace.The Government plans to get over 6 crore women on board to sell on the GeM platform.To enable this, the Government is empowering over 15 self-help groups with the Government’s public finance management system. Also, the Government plans to help provide easy loans to these SHGs with an app"""
    link="https://gem.gov.in/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)


@app.route('/govt2')
def govt2():
    name = "The Cent Kalyani Scheme"  
    title="The Cent Kalyani Scheme"
    pic="govt2.png"
    scheme="The Government Scheme for Women"
    content= """The Central Bank of India set up the Cent Kalyani Scheme with the main objective of encouraging women entrepreneurs to start a new project or expand their current one.
This Government scheme for entrepreneurs applies to self-employed women (doctors, consultants) and women engaged in manufacturing and serving industries.
The primary purpose of the scheme is to meet capital expenditure like Plant and Machinery/equipment as well as cash flow.
Under this Government scheme, you can access loans up to ₹1 crore sanctioned with a margin rate of 20%.  Interest on loans depends on market rates. The loan tenure will be a maximum of 7 years including a moratorium period of 6 months to 1 year.

"""
    link="https://www.startupindia.gov.in/content/sih/en/government-schemes/cent.html"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)

@app.route('/govt3')
def govt3():
    name = "Mudra Yojana Scheme For Women"  
    title="Mudra Yojana Scheme For Women"
    pic="govt3.png"
    scheme="The Government Scheme for Women"
    content= """The Mudra scheme aims to empower individual women entrepreneurs who want to start their own small businesses like tailoring units, tuition centres or schools etc.
The scheme also encourages women’s groups who want to start a business venture together.
The Mudra loan scheme requires zero collateral security. Also, it comes in 3 different criteria:
Shishu – Under this, the loan amount is limited to ₹ 50,000 and is mostly meant for new business ventures.
Kishor –  This schemes sanctions loans between₹ 50,000 to INR 5 lakhs and can be availed by those who have a well-established enterprise.
Tarun –  This Government scheme for women sanctions loans up to ₹ 10 lakhs and can also be availed by women-run small businesses which are well-established, but want to expand operations.
Post access to the Mudra loan, you avail a Mudra card which is similar to a credit card. The funds available are limited to 10% of the loan amount granted to you.

"""
    link="https://www.startupindia.gov.in/content/sih/en/government-schemes/cent.html"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)

@app.route('/govt4')
def govt4():
    name = "Orient Mahila Vikas Yojana scheme"  
    title="Orient Mahila Vikas Yojana scheme"
    pic="govt4.png"
    scheme="The Government Scheme for Women"
    content= """TLaunched by the Oriental Bank of Commerce this scheme provides capital for women for starting small businesses. Women entrepreneurs with a 51% share in their business are eligible for the loan. Women do not need to have collateral if loans are between ₹10 lakhs to ₹25 lakhs for small-scale industries.
The loan repayment time is 7 years and offers concession of 2% on the rate of interest.

"""
    link="https://www.govtgk.com/orient-mahila-vikas-yojana/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)

@app.route('/govt5')
def govt5():
    name = "Bhartiya Mahila Bank Business Loan"  
    title="Bhartiya Mahila Bank Business Loan"
    pic="govt5.png"
    scheme="The Government Scheme for Women"
    content= """The scheme became applied by using Bhartiya Mahila Bank (BMB) which was later merged with the State Bank of India in 2017. A public area banking enterprise established in 2013, it offered women entrepreneurs business loans as much as ₹20 Crores for assembly working capital requirement, commercial enterprise expansion, or production firms.
It additionally gives special business loans with a profitable fee of hobby and offers collateral-unfastened loans as much as ₹1 crore below CGTMSE (Credit Guarantee Fund Trust for Micro and Small Enterprises) cover.
Women entrepreneurs also are presented a 0.25 percentage concession in interest rate. It includes a mixture of operating capital and term loan. The repayment tenure is flexible and needs to be repaid inside seven years.

"""
    link="https://www.afinoz.com/business-loan/bhartiya-mahila-bank"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)

@app.route('/govt6')
def govt6():
    name = "Stree Shakti Package For Women Entrepreneurs "  
    title="Stree Shakti Package For Women Entrepreneurs "
    pic="govt6.png"
    scheme="The Government Scheme for Women"
    content= """The Stree Shakti Package is a unique SBI-run scheme to guide entrepreneurship amongst women with the aid of offering positive concessions. This scheme is eligible for women who’ve majority ownership (over 50 percent) in a small business. Another requirement is that these marketers must be enrolled inside the Entrepreneurship Development Programmes (EDP) prepared by their respective kingdom organization. This scheme allows girls to avail of a hobby concession of 0.05 percentage on loans exceeding ₹2 lakh. No security is needed for loans up to ₹5 lakh inside the case of small sector gadgets.
"""
    link="https://www.sbi.co.in/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)


@app.route('/govt7')
def govt7():
    name = "Support to training and employment programme(STEP) for women "  
    title="Support to training and employment programme(STEP) for women "
    pic="govt7.png"
    scheme="The Government Scheme for Women"
    content= """Ministry of Women & Child Development
STEP Scheme aims to provide skills that give employability to women and to provide competencies and skill that enable women to become self-employed/entrepreneurs. The Scheme is intended to benefit women who are in the age group of 16 years and above across the country.
"""
    link="https://www.startupindia.gov.in/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)


@app.route('/govt8')
def govt8():
    name = "Pradhan Mantri Kaushal Vikas Yojana"  
    title="Pradhan Mantri Kaushal Vikas Yojana "
    pic="govt8.png"
    scheme="The Government Scheme for Women"
    content= """ Though this scheme was not launched specifically for women, it does aim at providing skill training courses to women like beautician’s course, tailoring, handicrafts and jewellery making. It provided training, certification and even placements to the women who successfully complete the course. However, a theory exam needs to be cleared in order to obtain the certificate which poses a problem for illiterate women."""
    link=" http://pmkvyofficial.org/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)

@app.route('/govt9')
def govt9():
    name = "Skill India Scheme "  
    title="Skill India Scheme"
    pic="govt9.jpg"
    scheme="The Government Scheme for Women"
    content= """ Apprenticeship Training By National Skill Development Corporation under the Skill India Scheme is also provided to women. It is a pilot program in collaboration with UNDP and Society of Development Alternatives which aims to provide training to women in fifteen (15) months."""
    link=" https://www.skillindia.gov.in/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)


@app.route('/incb1')
def incu1():
    name = "Atal Incubation Centre (Goa Institute of Management)"  
    title="Atal Incubation Centre (Goa Institute of Management)"
    pic="incu1.jpg"
    scheme="Incubation Centers for Women"
    content= """ Atal Incubation Centre – Goa Institute of Management (AIC GIM) has been set up by Atal Innovations Mission (AIM) by NITI Aayog.  Our mission is to aid startups, stimulate their growth and facilitate their success through a hostilic support system for entrepreneurs by providing them opportunities to access mentors who are experts in their field of business, investment support, access to industries and networking with growing startup ecosystems."""
    link="https://www.aicgim.in"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)

@app.route('/incb2')
def incu2():
    name = "Virtual Incubation Program for Women Entrepreneurs (VIP-WE) by startupindia"  
    title="Virtual Incubation Program for Women Entrepreneurs (VIP-WE) by startupindia"
    pic="incu2.png"
    scheme="Incubation Centers for Women"
    content= """Zone Startups India is launching the 1st edition of Virtual Startup Incubation in collaboration with Startup India with a focus on tech-based innovations led by women entrepreneurs.

The Program will nurture 20 early-stage startups through a 2-month incubation journey that aims to support them in building their venture.

Along with Startup India, we aim to mentor the founders and also provide an extensive network of experts, corporates, and investors.

Additionally, the global strategic partnership with 100 Open Startup will enable startups to gain access to a global platform for their next level growth.

VIP-WE Objective - 

To catalyze tech-led innovation of 20 early-stage women-led startups.
"""
    link="https://www.startupindia.gov.in/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)

@app.route('/incb3')
def incu3():
    name = "Ciba"  
    title="Ciba"
    pic="incu3.jpg"
    scheme="Incubation Centers for Women"
    content= """Centre for Incubation & Business Acceleration a technology business incubator based in Goa and Mumbai supporting and nurturing startup companies by providing services such as incubation, modern office spaces, mentoring, networking opportunities, seed funding and rapid prototyping.
"""
    link="https://ciba.org.in/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)

@app.route('/incb4')
def incu4():
    name = "MEWO : COWORK NEST"  
    title="MEWO : COWORK NEST"
    pic="incu4.jpg"
    scheme="Incubation Centers for Women"
    content= """MeWo the brand represents “Meetings & Co-Working”. The concept is being launched by the founders to facilitate everything around Meetings & Co-Working for startups and corporates across the country who are exploring or who intend to start any business operations in Goa. The concept is a Joint Venture between Mr Abrar Shaikh & Mr Shrinivas Dempo. Our core focus is to make “Work Nests” for startups and corporates across the nation in Goa.   """
    link="https://mewo.co/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)

@app.route('/incb5')
def incu5():
    name = "91Springboard"  
    title="91Springboard"
    pic="incu5.jpg"
    scheme="Incubation Centers for Women"
    content= """ India's Leading Coworking Spaces in 27 locations, 9 cities Discover a new way of working Our coworking spaces play home to a diverse set of working professionals. Each with their own experiences, expertise and skills."""
    link="https://mewo.co/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)



@app.route('/incb6')
def incu6():
    name = "Forum for Innovation Incubation Research & Entrepreneurship"  
    title="Forum for Innovation Incubation Research & Entrepreneurship"
    pic="incu6.png"
    scheme="Incubation Centers for Women"
    content= """ FiiRE (Forum for Innovation Incubation Research & Entrepreneurship) is established with the support of Department of Science & Technology, Government of India under the National Initiative for Developing and Harnessing Innovations.
FiiRE is housed at the Don Bosco College of Engineering, Fatorda promoted by the Salesian Society, part of a massive network having an extensive reach over 130 countries. Currently, in India the Don Bosco Society has established over 500 institutes dedicated towards growth & development of youth.
"""
    link="https://www.fiire.org.in/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)


@app.route('/incb7')
def incu7():
    name = "IGNITE – EDC Innovation hub"  
    title="IGNITE – EDC Innovation hub"
    pic="incu7.jpg"
    scheme="Incubation Centers for Women"
    content= """ IGNITE – EDC Innovation Hub by EDC Ltd, Goa is a high-quality facility, conceived to be an INCUBATION CENTER and a COWORKING SPACE. We aim to empower budding entrepreneurs to succeed and grow strong, scalable & successful ventures, thereby creating value for their founders, teams and the State of Goa.
The center is a sprawling 5000 sq. ft. area at EDC House, Panaji, Goa with state-of-the-art facilities to provide collaborative working, while maintaining privacy and encouraging innovation and creativity.
The core team at IGNITE EDC Innovation Hub includes experienced professionals and consultants with a track record of setting up & running Incubators across the Country. The center is managed with an open and collaborative leadership translating into positive attitude and growth.
"""
    link="https://edcignite.com/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)

@app.route('/incb8')
def incu8():
    name = "BITS BIRAC BIONEST"  
    title="BITS BIRAC BIONEST"
    pic="incu8.jpg"
    scheme="Incubation Centers for Women"
    content= """  BITS BIRAC BioNEST incubator, an initiative of CIIE of Birla Institute of Technology and Science, Pilani, K K Birla Goa Campus promotes innovation and entrepreneurship in Health & Environment. BioNEST Goa is supported by BIRAC (Biotechnology Industry Research Assistance Council), a Non-profit organization under Department of Biotechnology (DBT), Government of India. BioNEST aims to help entrepreneurs to ideate, incubate and accelerate their innovative early stage start ups into successful ventures through infrastructural support, mentoring, networking and business advisory. The incubator brings entrepreneurs, mentors, researchers and academicians together to create a vibrant startup ecosystem. Be a part of our network to participate in stimulating conversations, innovative thinking and create forward-looking startups. Together, let us ignite the spark of new ideas and ventures"""
    link="https://www.bits-pilani.ac.in/Goa/BITSBIRAC/"
    return render_template("1govt.html",name=name,title=title,content=content,pic=pic,link=link)



if __name__ == "__main__":
    app.run(debug=True)















