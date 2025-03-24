import qrcode 
#taking upi id user

upi_id=input("enter your upi id=")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

phonepay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


#make Qr code

phonepay_qr=qrcode.make(phonepay_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

#save your Qr code in your file 

phonepay_qr.save("phonepay_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_qr.png")

#Display QR CODE 

phonepay_qr.show()
paytm_qr.show()
google_pay_qr.show()