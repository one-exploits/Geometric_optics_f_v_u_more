def Rightinput(datatype):
	if datatype=="int()":
		while True:
			try:
				intinput=int(input());
				return intinput;
				break;	
			except:
				print("error input integer value *\n");
				continue;
					

#Home and option
def home():
	print("\t  Mobile Num- 7007030997");
	print("       YouTube channel- One-EXPLOITs'\n");
	print("\n[1] Calculate focal length 'f'");
	print("[2] Calculate image distance 'v'");
	print("[3] Calculate object distance 'u'");

#calculate focal 
def ffocal(v,u):
	focal_d=((v)*(u))/(u+v);
	return focal_d;


#calculate image distance
def vimage(f,u):
	image_d=((u)*(f))/(u-f)
	return image_d;


#calculate object distance:
def uobject(f,v):
	object_d=((v)*(f))/(v-f);
	return object_d;

def user_input_and_ans():
#-------------###----------------#	
	option=Rightinput("int()");
	if(option==1):
		v=float(input("\nEnter 'v':"))
		u=float(input("Enter 'u':"))
		Ans=ffocal(v,u);
		return Ans;
		
	elif(option==2):
		f=float(input("\nEnter 'f':"))
		u=float(input("Enter 'u':"))
		Ans=vimage(f,u);
		return Ans;
	
	elif(option==3):
		f=float(input("\nEnter 'f':"))
		v=float(input("Enter 'v':"))
		Ans=uobject(f,v);
		return Ans

def main():
	if(__name__=="__main__"):
		home();
		print(user_input_and_ans());
		
main()
	