# Custom script to provide shared utility function to all mlproject runs.

#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 

# This script silences the pydantic warnings for unsupported field attributes
'''
def silence_pydantic_warnings():
    """
    Best-effort silencer for Pydantic warnings. 
    Never raises — allows all other code to continue even on failure.
    """
    try:
        import warnings
        try:
            from pydantic.warnings import UnsupportedFieldAttributeWarning
            warnings.filterwarnings("ignore", category=UnsupportedFieldAttributeWarning)
        except Exception:
            # If pydantic is missing or the class name changed, do nothing
            pass
    except Exception:
        # If even importing warnings fails (very unlikely), still no-op
        pass
'''

#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 

# Updated Version: This version suppresses warnings for Unsported Field Attribute and Pydantic Deprecated Since 20

def silence_pydantic_warnings():
    """
    Best-effort silencer for Pydantic warnings. 
    Never raises — allows all other code to continue even on failure.
    """

    diagnostic_flag = False
    try:
        import warnings
        try:
            # Import categories if available (pydantic v2)
            from pydantic.warnings import (
                UnsupportedFieldAttributeWarning,
                PydanticDeprecatedSince20,
            )
            warnings.filterwarnings("ignore", category=UnsupportedFieldAttributeWarning)
            warnings.filterwarnings("ignore", category=PydanticDeprecatedSince20)
        except Exception as e:
            # If pydantic is missing or names changed, just ignore silently
            # pass
            if diagnostic_flag:
                print(f"Import/Setup Failed, Skipping: {e}")
    except Exception as e:
        # If even importing warnings fails (extremely unlikely), still no-op
        # pass
        if diagnostic_flag:
            print(f"Warning Suppression Failed, Skipping: {e}")

#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### 

