// Usage Examples
//
// LMS demo
// removes 50Hz from an Audio signal with a powerline reference
// here generated with a simple sine. Should be ideally
// also measured with another ADC channel and fed into
// the filter.

// This is the only include you need
#include <Fir1.h>
#include <iostream>
#include <iomanip>

#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define NTAPS 500
#define LEARNING_RATE 0.005

int main (int,char**)
{
	// inits the filter
	Fir1 fir(NTAPS);
	fir.setLearningRate(LEARNING_RATE);

	FILE *finput = fopen("recording2voxs+n.dat","rt");
	FILE *foutput = fopen("recfilteredout.dat","wt");
	FILE *finputref = fopen("recording2bassn.dat","rt");
      
	
	for(int i=0;i<1510000;i++) //i<no. of samples in voxs+n
	{
	  float input_signal, timestamp1;		
	  fscanf(finput,"%f %f\n",&timestamp1, &input_signal);
	  
	  float ref_noise, timestamp2;
	  fscanf(finputref, "%f %f/n",&timestamp2, &ref_noise);  
	  //float ref_noise = sin(2*M_PI/20*i);
	  
	  float canceller = fir.filter(ref_noise);
	  float output_signal = (input_signal - sin(2*M_PI/20))- (canceller - sin(2*M_PI/20)); //50Hz mains removal
    

	  
	  fir.lms_update(output_signal); 
	  fprintf(foutput,"%f %f %f\n",output_signal,canceller,ref_noise);
	}
	
	fclose(finput);
	fclose(foutput);
	fclose(finputref);
	fprintf(stderr,"Written the filtered ECG to 'recfilteredout.dat'\n");
}
