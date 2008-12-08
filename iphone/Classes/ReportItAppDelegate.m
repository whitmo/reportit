//
//  ReportItAppDelegate.m
//  ReportIt
//
//  Created by Anil Makhijani on 12/7/08.
//  Copyright Spacial Distillery 2008. All rights reserved.
//

#import "ReportItAppDelegate.h"

@implementation ReportItAppDelegate

@synthesize window;


- (void)applicationDidFinishLaunching:(UIApplication *)application {    

    // Override point for customization after application launch
    [window makeKeyAndVisible];
}


- (void)dealloc {
    [window release];
    [super dealloc];
}


@end
