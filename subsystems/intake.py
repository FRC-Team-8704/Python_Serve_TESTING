import rev

class IntakeSubsystem:
    def __init__(self):
        # All hardware setup stays here
        self.intake_motor = rev.SparkMax(9, rev.SparkLowLevel.MotorType.kBrushed)
        self.launch_motor = rev.SparkMax(10, rev.SparkLowLevel.MotorType.kBrushed)
        
        config = rev.SparkMaxConfig()
        config.setIdleMode(rev.SparkMaxConfig.IdleMode.kCoast)
        
        self.intake_motor.configure(config, rev.ResetMode.kResetSafeParameters, rev.PersistMode.kPersistParameters)

    def run_intake(self, speed):
        self.intake_motor.set(speed)
        self.launch_motor.set(speed) 
    
    def launch(self, speed):
        self.intake_motor.set(-speed)
        self.launch_motor.set(speed) 

    def stop(self):
        self.intake_motor.set(0)
        self.launch_motor.set(0)