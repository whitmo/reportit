//
//  ReporterViewController.m
//  ReportIt
//
//  Created by Anil Makhijani on 12/7/08.
//  Copyright 2008 Spacial Distillery. All rights reserved.
//

#import "ReporterViewController.h"

@implementation ReporterViewController

@synthesize txtProblem, lblMessage, sProblem;

- (IBAction) sendProblem:(id)sender {	
	NSString* tempMessage;
	tempMessage = [[NSString alloc] initWithFormat:@"Sent!  Thank you for reporting!"];
	lblMessage.text = tempMessage;
	[tempMessage release];
}


- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil {
	if (self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil]) {
		// Initialization code
	}
	return self;
}

/*
 Implement loadView if you want to create a view hierarchy programmatically
 - (void)loadView {
 }
 */

/*
 If you need to do additional setup after loading the view, override viewDidLoad.
 - (void)viewDidLoad {
 }
 */


- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation {
	// Return YES for supported orientations
	return (interfaceOrientation == UIInterfaceOrientationPortrait);
}


- (void)didReceiveMemoryWarning {
	[super didReceiveMemoryWarning]; // Releases the view if it doesn't have a superview
	// Release anything that's not essential, such as cached data
}

- (BOOL)textFieldShouldReturn:(UITextField *)theTextField {
	if(theTextField == txtProblem) {
		[txtProblem resignFirstResponder];
	}
	
	return YES;
}


- (void)dealloc {
	[txtProblem release];
	[lblMessage release];
	[sProblem release];
    [super dealloc];
}


@end


