//
//  ReportItAppDelegate.m
//  ReportIt
//
//  Created by Anil Makhijani on 12/7/08.
//  Copyright Spacial Distillery 2008. All rights reserved.
//

#import "ReportItAppDelegate.h"
#import "ReporterViewController.h"

@implementation ReportItAppDelegate

@synthesize window, viewController;


- (void)applicationDidFinishLaunching:(UIApplication *)application {    

	ReporterViewController *vController = [[ReporterViewController alloc]
										   initWithNibName:@"reporter" bundle:[NSBundle mainBundle]];
	
	self.viewController = vController;
	
	[vController release];
	
	[window addSubview:[viewController view]];
	
    // Override point for customization after application launch
    [window makeKeyAndVisible];
}




- (void)dealloc {
	[viewController release];
    [window release];
    [super dealloc];
}


@end
