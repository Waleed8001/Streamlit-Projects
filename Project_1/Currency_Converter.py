import streamlit as st
import requests
import time

st.set_page_config(
    page_title="Currency Converter",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

API_KEY = "f24c75b0a4b46ac8a65ccd1f"

currency = {
    "USD" : "United States Dollar",
    "AED" : "United Arab Emirates Dirham",
    "AFN" : "Afghanistan Afghani",
    "ALL" : 'Albania Lek',
    "AMD" : 'Armenia Dram',
    "ANG" : 'Netherlands Antillean Guilder (Curaçao, Sint Maarten)',
    "AOA" : 'Angola Kwanza',
    "ARS" : 'Argentina Peso',
    "AUD" : 'Australia Dollar',
    "AWG" : 'Aruba Florin',
    "AZN" : 'Azerbaijan Manat',
    "BAM" : 'Bosnia and Herzegovina Convertible Mark',
    "BBD" : 'Barbados Dollar',
    "BDT" : 'Bangladesh Taka',
    "BGN" : 'Bulgaria Lev',
    "BHD" : 'Bahrain Dinar',
    "BIF" : 'Burundi Franc',
    "BMD" : 'Bermuda Dollar',
    "BND" : 'Brunei Dollar',
    "BOB" : 'Bolivia Boliviano',
    "BRL" : 'Brazil Real',
    "BSD" : 'Bahamas Dollar',
    "BTN" : 'Bhutan Ngultrum',
    "BWP" : 'Botswana Pula',
    "BYN" : 'Belarus Ruble',
    "BZD" : 'Belize Dollar',
    "CAD" : 'Canada Dollar',
    "CDF" : 'Democratic Republic of the Congo Franc',
    "CHF" : 'Switzerland Franc',
    "CLP" : 'Chile Peso',
    "CNY" : 'China Yuan Renminbi',
    "COP" : 'Colombia Peso',
    "CRC" : 'Costa Rica Colon',
    "CUP" : 'Cuba Peso',
    "CVE" : 'Cape Verde Escudo',
    "CZK" : 'Czech Republic Koruna',
    "DJF" : 'Djibouti Franc',
    "DKK" : 'Denmark Krone',
    "DOP" : 'Dominican Republic Peso',
    "DZD" : 'Algeria Dinar',
    "EGP" : 'Egypt Pound',
    "ERN" : 'Eritrea Nakfa',
    "ETB" : 'Ethiopia Birr',
    "EUR" : 'Euro (Eurozone countries)',
    "FJD" : 'Fiji Dollar',
    "FKP" : 'Falkland Islands Pound',
    "FOK" : 'Faroe Islands Króna',
    "GBP" : 'United Kingdom Pound Sterling',
    "GEL" : 'Georgia Lari',
    "GGP" : 'Guernsey Pound',
    "GHS" : 'Ghana Cedi',
    "GIP" : 'Gibraltar Pound',
    "GMD" : 'Gambia Dalasi',
    "GNF" : 'Guinea Franc',
    "GTQ" : 'Guatemala Quetzal',
    "GYD" : 'Guyana Dollar',
    "HKD" : 'Hong Kong Dollar',
    "HNL" : 'Honduras Lempira',
    "HRK" : 'Croatia Kuna',
    "HTG" : 'Haiti Gourde',
    "HUF" : 'Hungary Forint',
    "IDR" : 'Indonesia Rupiah',
    "IMP" : 'Isle of Man Pound',
    "INR" : 'India Rupee',
    "IQD" : 'Iraq Dinar',
    "IRR" : 'Iran Rial',
    "ISK" : 'Iceland Krona',
    "JEP" : 'Jersey Pound',
    "JMD" : 'Jamaica Dollar',
    "JOD" : 'Jordan Dinar',
    "JPY" : 'Japan Yen',
    "KES" : 'Kenya Shilling',
    "KGS" : 'Kyrgyzstan Som',
    "KHR" : 'Cambodia Riel',
    "KID" : 'Kiribati Dollar',
    "KMF" : 'Comoros Franc',
    "KRW" : 'South Korea Won',
    "KWD" : 'Kuwait Dinar',
    "KYD" : 'Cayman Islands Dollar',
    "KZT" : 'Kazakhstan Tenge',
    "LAK" : 'Laos Kip',
    "LBP" : 'Lebanon Pound',
    "LKR" : 'Sri Lanka Rupee',
    "LRD" : 'Liberia Dollar',
    "LSL" : 'Lesotho Loti',
    "LYD" : 'Libya Dinar',
    "MAD" : 'Morocco Dirham',
    "MDL" : 'Moldova Leu',
    "MGA" : 'Madagascar Ariary',
    "MKD" : 'North Macedonia Denar',
    "MMK" : 'Myanmar Kyat',
    "MNT" : 'Mongolia Tugrik',
    "MOP" : 'Macao Pataca',
    "MRU" : 'Mauritania Ouguiya',
    "MUR" : 'Mauritius Rupee',
    "MVR" : 'Maldives Rufiyaa',
    "MWK" : 'Malawi Kwacha',
    "MXN" : 'Mexico Peso',
    "MYR" : 'Malaysia Ringgit',
    "MZN" : 'Mozambique Metical',
    "NAD" : 'Namibia Dollar',
    "NGN" : 'Nigeria Naira',
    "NIO" : 'Nicaragua Córdoba',
    "NOK" : 'Norway Krone',
    "NPR" : 'Nepal Rupee',
    "NZD" : 'New Zealand Dollar',
    "OMR" : 'Oman Rial',
    "PAB" : 'Panama Balboa',
    "PEN" : 'Peru Sol',
    "PGK" : 'Papua New Guinea Kina',
    "PHP" : 'Philippines Peso',
    "PKR" : 'Pakistan Rupee',
    "PLN" : 'Poland Zloty',
    "PYG" : 'Paraguay Guarani',
    "QAR" : 'Qatar Riyal',
    "RON" : 'Romania Leu',
    "RSD" : 'Serbia Dinar',
    "RUB" : 'Russia Ruble',
    "RWF" : 'Rwanda Franc',
    "SAR" : 'Saudi Arabia Riyal',
    "SBD" : 'Solomon Islands Dollar',
    "SCR" : 'Seychelles Rupee',
    "SDG" : 'Sudan Pound',
    "SEK" : 'Sweden Krona',
    "SGD" : 'Singapore Dollar',
    "SHP" : 'Saint Helena Pound',
    "SLE" : 'Sierra Leone Leone (new)',
    "SLL" : 'Sierra Leone Leone (old)',
    "SOS" : 'Somalia Shilling',
    "SRD" : 'Suriname Dollar',
    "SSP" : 'South Sudan Pound',
    "STN" : 'São Tomé and Príncipe Dobra',
    "SYP" : 'Syria Pound',
    "SZL" : 'Eswatini Lilangeni',
    "THB" : 'Thailand Baht',
    "TJS" : 'Tajikistan Somoni',
    "TMT" : 'Turkmenistan Manat',
    "TND" : 'Tunisia Dinar',
    "TOP" : 'Tonga Paʻanga',
    "TRY" : 'Türkiye Lira',
    "TTD" : 'Trinidad and Tobago Dollar',
    "TVD" : 'Tuvalu Dollar',
    "TWD" : 'Taiwan Dollar',
    "TZS" : 'Tanzania Shilling',
    "UAH" : 'Ukraine Hryvnia',
    "UGX" : 'Uganda Shilling',
    "UYU" : 'Uruguay Peso',
    "UZS" : 'Uzbekistan Som',
    "VES" : 'Venezuela Bolívar Soberano',
    "VND" : 'Vietnam Dong',
    "VUV" : 'Vanuatu Vatu',
    "WST" : 'Samoa Tala',
    "XAF" : 'Central African CFA Franc (BEAC countries)',
    "XCD" : 'East Caribbean Dollar',
    "XCG" : '(Non-standard, likely typo — probably should be ANG/Aruba Florin duplicate)',
    "XDR" : 'IMF Special Drawing Rights',
    "XOF" : 'West African CFA Franc (UEMOA countries)',
    "XPF" : 'CFP Franc (French Pacific territories)',
    "YER" : 'Yemen Riyal',
    "ZAR" : 'South Africa Rand',
    "ZMW" : 'Zambia Kwacha',
    "ZWL" : 'Zimbabwe Dollar'
}


st.session_state.coun = []
    
# if "coun" not in st.session_state:
# st.session_state.calculate = 0.0

for key, value in currency.items():
    st.session_state.coun.append(key + " - " + value)
    
st.session_state.coun.sort()
# print(coun)
# print(currency)
st.header("💸 Welcome to :green[Currency Convertor] App", divider="orange")

def choose_country(my_key):
    c = st.selectbox(
        "Select Currency",
        st.session_state.coun,
        index=None,
        placeholder="PKR",
        accept_new_options=True,
        key=my_key
    )
    
    return c

c1 = c2 = None


c1 = choose_country("Country_1")

if c1 is not None:
    c1 = c1[:3]

num = st.number_input("Enter Number", min_value=0)

c2 = choose_country("Country_2")

if c2 is not None:
    c2 = c2[:3]
    
st.divider()

convert = st.button("Convert", use_container_width=True)
if convert:
    if c1 and c2:
        progress_text = f"Converting {c1} to {c2}. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.001)
            my_bar.progress(percent_complete + 1, text=progress_text)
            
        time.sleep(1)
        my_bar.empty()
    
        example = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{c1}"
        if c1:
            currency_2 = requests.get(example).json()['conversion_rates']
            # print(currency_2)

        calculate = currency_2[c1] * currency_2[c2] * num
        # st.write(f"{c1} to {c2}: ", calculate)
        st.markdown(f"<p style='font-size:20px;'>{c1} to {c2}: {calculate}</p>", unsafe_allow_html=True)
        st.balloons()

    else:
        st.error("Please select a Valid Country")

# st.header("Welcome to my Portfolio")
# st.header("WOW")
# c2 = st.selectbox(
#     "Select Currency",
#     st.session_state.coun,
#     index=None,
#     placeholder="PKR",
#     accept_new_options=True,
#     key="curr_2"
# )