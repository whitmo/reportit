//
//  ReporterViewController.h
//  ReportIt
//
//  Created by Anil Makhijani on 12/7/08.
//  Copyright 2008 Spacial Distillery. All rights reserved.
//

#import <UIKit/UIKit.h>


@interface ReporterViewController : UIViewController <UITextFieldDelegate> {
	
    IBOutlet UITextField *txtProblem;
	IBOutlet UILabel *lblMessage;
	NSString *sProblem;
}

@property (nonatomic, retain) IBOutlet UITextField *txtProblem;
@property (nonatomic, retain) IBOutlet UILabel *lblMessage;
@property (nonatomic, copy) NSString *sProblem;

-(IBAction)sendProblem:(id)sender;

@end


