# Frequently asked questions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/new-data-prep-faqs.html](https://docs.aws.amazon.com/quick/latest/userguide/new-data-prep-faqs.html)

---

## 1. When do users need to switch from the new to legacy experience?

    		
    		Users must return to the legacy experience when working with datasets that contain currently 
    			[unsupported features](./unsupported-features.html). Quick Sight is actively working 
    			to incorporate these features into the new experience in upcoming releases.

## 2. Why are datasets grayed out when trying to add them in the new experience? Can datasets be combined between legacy and new experiences?

    		
    		Currently, parent and child datasets must exist within the same experience environment. You cannot combine datasets across legacy and new experiences because the new experience includes additional features not available in legacy, such as Append functionalities, Pivot capabilities, and Divergence.

**Using parent datasets from the legacy experience**

To use parent datasets from the legacy experience, you can switch back to that environment. Simply navigate to the data 
    			preparation page and choose **Switch back to legacy experience** in the top right corner. Once 
    			there, you can create your child datasets as needed.

**Future development**

We are planning to implement functionality that will allow users to upgrade legacy datasets to the new experience. This upgraded pathway will enable the use of legacy parent datasets within the new experience.

## 3. Why is Quick Sight launching the new data preparation experience before achieving full feature parity with the legacy experience?

            
            The new data preparation experience was developed through extensive customer collaboration to address real-world analytics challenges. The initial launch prioritizes:

**Enhanced capabilities**

- 
                    Visual transformation workflows 
- 
                    Improved process transparency 
- 
                    Advanced preparation techniques through Divergence 
- 
                    Powerful new features like Append, Aggregate, and Pivot 

**Flexible adoption**

Users can choose between experiences before publishing datasets, ensuring uninterrupted workflows while teams transition at their own pace. This approach allows immediate access to new capabilities while maintaining support for specialized requirements through the legacy experience.

## 4. Will features currently available only in the legacy experience be added to the new experience?

            
            Yes. Quick Sight is actively working to incorporate legacy features into the new experience.

## 5. How do API changes affect existing dataset creation scripts?

            
            Quick Sight maintains backwards compatibility while introducing new capabilities:

- 
                    Existing Scripts: Legacy API scripts will continue to function, creating datasets in the legacy experience 
- 
                    API Naming: Current API names remain unchanged 
- 
                    New Functionality: Additional API formats support the new experience's enhanced capabilities 
- 
                    Documentation: Complete API specifications for the new experience are available in our API reference 

## 6. Can datasets be converted between experiences after publication?

   
            - 
                	Future Migration Path: Quick Sight will add a feature in the future to easily migrate legacy datasets to the new experience. 
- 
                    One-Way Process: Converting datasets from the new experience to legacy format isn't supported due to advanced feature dependencies