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
	[[MyCLController sharedInstance].locationManager startUpdatingLocation];
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

 - (void)viewDidLoad {
	 [MyCLController sharedInstance].delegate = self;
 }


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

- (void)newLocationUpdate:(NSString *)status latitude: (float)latitude longitude: (float)longitude timeStamp: (NSString *)timeStamp {
	
	NSString *tempMessage = nil;
	
	NSString *eyesServer = nil;
	eyesServer = [[NSString alloc] initWithFormat:@"http://novalis.org/cgi/location.cgi"];
	
	NSString *postContent = nil;
	postContent = [[NSString alloc] initWithFormat:@"report=%@&lat=%f&lng=%f&date=%@", txtProblem.text, latitude, longitude, timeStamp];
	
	// url is set to be some URL string.
	NSMutableURLRequest* post = [NSMutableURLRequest requestWithURL: [NSURL URLWithString: eyesServer]];
	[post setHTTPMethod: @"POST"];
	[post setHTTPBody: [[[NSString alloc] initWithString: postContent] 
						dataUsingEncoding: NSASCIIStringEncoding]];
	
	NSURLConnection* theConnection = [NSURLConnection connectionWithRequest: post
																   delegate: self];
	[theConnection retain];
	
	
	tempMessage = [[NSString alloc] initWithFormat:@"Sent!  Thank you for reporting!"];
	
	lblMessage.text = tempMessage;
	
	
	[eyesServer release];
	
	[tempMessage release];
	//[[MyCLController sharedInstance].locationManager stopUpdatingLocation];
	
	
}


-(void)newError:(NSString *)text {
	
}


- (void)dealloc {
	[txtProblem release];
	[lblMessage release];
	[sProblem release];
    [super dealloc];
}


@end


