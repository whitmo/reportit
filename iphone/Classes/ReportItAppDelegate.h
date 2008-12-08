//
//  ReportItAppDelegate.h
//  ReportIt
//
//  Created by Anil Makhijani on 12/7/08.
//  Copyright Spacial Distillery 2008. All rights reserved.
//

#import <UIKit/UIKit.h>

@class ReporterViewController;

@interface ReportItAppDelegate : NSObject <UIApplicationDelegate> {
    IBOutlet UIWindow *window;
	ReporterViewController *viewController;
}

@property (nonatomic, retain) UIWindow *window;
@property (nonatomic, retain) ReporterViewController *viewController;

@end

